import numpy as np
import operator
import random
np.random.seed(0)

n = int(input("Insert no of delay count :"))
fifo_ex_no_customers_in_q = 0.0
fifo_ex_uti_s1 = 0.0
fifo_ex_uti_s2 = 0.0

lifo_ex_no_customers_in_q = 0.0
lifo_ex_uti_s1 = 0.0
lifo_ex_uti_s2 = 0.0

sjf_ex_no_customers_in_q = 0.0
sjf_ex_uti_s1 = 0.0
sjf_ex_uti_s2 = 0.0

avgd1 = 0.0
avgd2 = 0.0
avgd3 = 0.0
t1 = 0.0
t2 = 0.0
t3 = 0.0

iat = [0.4, 1.2, 0.5, 1.7, 0.2, 1.6, 0.2, 1.4, 1.9, 0.7]
st = [2.0, 0.7, 0.2, 1.1, 3.7, 0.6]

for i in range(500):
    temp = np.random.exponential(1/3.0)
    iat.append(temp)

    temp = np.random.exponential(1/3.0)
    st.append(temp)




class fifo:
  def __init__(self): #initializing all the var of fifo
    self.interarrivals= iat.copy()
    self.service_times= st.copy()
    print(self.interarrivals)
    print(self.service_times)
    self.clock = 0.0

    self.next_arrival = self.interarrivals.pop(0)
    self.next_departure1 = float('inf')
    self.next_departure2 = float('inf')

    self.num_in_queue = 0
    self.times_of_arrivalqueue = []     #store times of arrivals who are waiting in the queue
    self.service_times_in_queue = []  #store service times of waiting customers in the queue

    self.total_delay = 0.0
    self.num_of_delays = 0.0
    self.area_under_qt = 0.0
    self.area_under_bt1 = 0.0
    self.area_under_bt2 = 0.0
    self.number_of_customers_in_q = 0.0

    self.server_status1 = 0
    self.server_status2 = 0  #0 for IDLE , 1 for BUSY
    self.last_event_time = 0.0  #we will need to store last event clock time

  def start(self):
    while self.num_of_delays <= n:
      self.timing()

  def timing(self):
    self.clock = min(self.next_arrival, self.next_departure1, self.next_departure2)  # First set clock to minimum time of next event
    self.update_register()

    if self.next_arrival < self.next_departure1 and self.next_arrival < self.next_departure2:
      print("Arrival at Clock:" + str(self.clock))
      self.arrival()

    elif self.next_departure1 < self.next_departure2:
      print("Departure of server 1 at " + str(self.clock))
      self.departure1()

    else:
      print("Departure of server 2 at " + str(self.clock))
      self.departure2()


    print("Server-1 Status :" + str(self.server_status1))
    print("Server-2 Status :" + str(self.server_status2))
    print("Times of arrivals in Queue: " + str(self.times_of_arrivalqueue))
    print("Service times in Queue: " + str(self.service_times_in_queue))
    print("Number of Delays: " + str(self.num_of_delays))
    print("Total Delay:" + str(self.total_delay))
    print("Area under QT:" + str(self.area_under_qt))
    print("Area under BT1:" + str(self.area_under_bt1))
    print("Area under Bt2:" + str(self.area_under_bt2))
    print("Next Arrival Time: " + str(self.next_arrival))
    print("Next Departure Time of server-1: " + str(self.next_departure1))
    print("Next Departure Time of server-2: " + str(self.next_departure2))
    print("Expected average Delay:" + str(self.total_delay / n))
    self.number_of_customers_in_q = len(self.service_times_in_queue) + self.number_of_customers_in_q
    print("Average number of customers in queue:" + str(self.number_of_customers_in_q / n))
    print("\n--------------------------------------------\n")

    if self.num_of_delays == n:
      global avgd1
      global t1
      avgd1 = self.total_delay
      t1 = self.clock

  def arrival(self):
            #Schedule next arrival , new_arrival = previous_arrival + inter_arrival time of next customer
    self.next_arrival += self.interarrivals.pop(0)

    if self.server_status1 == 0:  #server is idle
      self.server_status1 = 1  #make server BUSY
      delay = 0.0  #so delay is zero
      self.total_delay += delay
      self.num_of_delays += 1  #increase the number of customers delayed

      self.next_departure1 = self.clock + self.service_times.pop(0)

    elif self.server_status2 == 0:  #server is idle
      self.server_status2 = 1  #make server BUSY
      delay = 0.0  #so delay is zero
      self.total_delay += delay
      self.num_of_delays += 1  #increase the number of customers delayed

                #schedule next departure, pop the first element of service_times list to get service time of this customer
      self.next_departure2 = self.clock + self.service_times.pop(0)

    else:  #Server is BUSY
                #increase queue length, this customer will have to wait in the queue
      self.num_in_queue += 1

                #store the arrival time and service time of this customer in seperate lists
      self.times_of_arrivalqueue.append(self.clock)
      self.service_times_in_queue.append(self.service_times.pop(0))

  def departure1(self):
            #check number of customers in the queue
    if self.num_in_queue == 0:  # if no customer in the queue
                #make server IDLE
      self.server_status1 = 0
                #schedule next departure= infinity
      self.next_departure1 = float('inf')

    else:
                #if queue not empty, pop one customer, decrease queue length
      self.num_in_queue -= 1
      self.num_of_delays += 1
                #AS FIFO, pop first arrival and service time from the queue. IF LIFO we have to pop last arrival and service time
                #For SJF, finf the index of minimum service time from  service_times_in_queue list.
                #Then pop the arrival of that index from times_of_arrivalqueue for delay count and others.

      arrival = self.times_of_arrivalqueue.pop(0)

      delay = self.clock - arrival
      self.total_delay += delay
      self.next_departure1 = self.clock + self.service_times_in_queue.pop(0)

  def departure2(self):
            #check number of customers in the queue
    if self.num_in_queue == 0:  # if no customer in the queue
      self.server_status2 = 0        
      self.next_departure2 = float('inf')

    else:
                #if queue not empty, pop one customer, decrease queue length
      self.num_in_queue -= 1
      self.num_of_delays += 1
                #AS FIFO, pop first arrival and service time from the queue. IF LIFO we have to pop last arrival and service time
                #For SJF, finf the index of minimum service time from  service_times_in_queue list.
                #Then pop the arrival of that index from times_of_arrivalqueue for delay count and others.

      arrival = self.times_of_arrivalqueue.pop(0)

      delay = self.clock - arrival
      self.total_delay += delay
      self.next_departure2 = self.clock + self.service_times_in_queue.pop(0)



  def update_register(self):
    global fifo_ex_no_customers_in_q
    global fifo_ex_uti_s1
    global fifo_ex_uti_s2
    time_differnce = self.clock - self.last_event_time
    self.area_under_qt += self.num_in_queue * time_differnce
    fifo_ex_no_customers_in_q= fifo_ex_no_customers_in_q + self.num_in_queue * time_differnce
    self.area_under_bt1 += self.server_status1 * time_differnce
    fifo_ex_uti_s1 = fifo_ex_uti_s1 + self.server_status1 * time_differnce
    self.area_under_bt2 += self.server_status2 * time_differnce
    fifo_ex_uti_s2 = fifo_ex_uti_s2 + self.server_status2 * time_differnce
    self.last_event_time = self.clock


class lifo:
  def __init__(self):

    self.interarrivals= iat.copy()
    self.service_times= st.copy()
    #print(self.interarrivals)
    #print(self.service_times)
    self.clock = 0.0

    self.next_arrival = self.interarrivals.pop(0)
    self.next_departure1 = float('inf')
    self.next_departure2 = float('inf')

    self.num_in_queue = 0
    self.times_of_arrivalqueue = []  #store times of arrivals who are waiting in the queue
    self.service_times_in_queue = []  #store service times of waiting customers in the queue

    self.total_delay = 0.0
    self.num_of_delays = 0.0
    self.area_under_qt = 0.0
    self.area_under_bt1 = 0.0
    self.area_under_bt2 = 0.0
    self.number_of_customers_in_q = 0.0

    self.server_status1 = 0
    self.server_status2 = 0  #0 for IDLE , 1 for BUSY
    self.last_event_time = 0.0  #we will need to store last event clock time

        
  def start(self):
    while self.num_of_delays <= n:
      self.timing()

  def timing(self):
    self.clock = min(self.next_arrival, self.next_departure1, self.next_departure2)  # First set clock to minimum time of next event
    self.update_register()

    if self.next_arrival < self.next_departure1 and self.next_arrival < self.next_departure2:
      print("Arrival at Clock:" + str(self.clock))
      self.arrival()

    elif self.next_departure1 < self.next_departure2:
      print("Departure at Clock(server-1) :" + str(self.clock))
      self.departure1()

    elif self.next_departure2 < self.next_departure1:
      print("Departure at Clock(server-2) :" + str(self.clock))
      self.departure2()


    print("Server-1 Status :" + str(self.server_status1))
    print("Server-2 Status :" + str(self.server_status2))
    print("Times of arrivals in Queue: " + str(self.times_of_arrivalqueue))
    print("Service times in Queue: " + str(self.service_times_in_queue))
    print("Number of Delays: " + str(self.num_of_delays))
    print("Total Delay:" + str(self.total_delay))
    print("Area under QT:" + str(self.area_under_qt))
    print("Area under BT1:" + str(self.area_under_bt1))
    print("Area under Bt2:" + str(self.area_under_bt2))
    print("Next Arrival Time: " + str(self.next_arrival))
    print("Next Departure Time of server-1: " + str(self.next_departure1))
    print("Next Departure Time of server-2: " + str(self.next_departure2))
    print("Expected average Delay:" + str(self.total_delay / n))
    self.number_of_customers_in_q = len(self.service_times_in_queue) + self.number_of_customers_in_q
    print("Average number of customers in queue:" + str(self.number_of_customers_in_q / n))
    print("\n--------------------------------------------\n")

    if self.num_of_delays == n:
      global avgd2
      global t2
      avgd2 = self.total_delay
      t2 = self.clock

  def arrival(self):
    self.next_arrival += self.interarrivals.pop(0)

    if self.server_status1 == 0: #server Idle
      self.server_status1 = 1  #make server BUSY
      delay = 0.0           #so delay is zero
      self.total_delay += delay
      self.num_of_delays += 1  #increase the number of customers delayed

      self.next_departure1 = self.clock + self.service_times.pop(0)

    elif self.server_status2 == 0:  #server is idle
      self.server_status2 = 1  #make server BUSY
      delay = 0.0  #so delay is zero
      self.total_delay += delay
      self.num_of_delays += 1  #increase the number of customers delayed

      #schedule next departure, pop the first element of service_times list to get service time of this customer
      self.next_departure2 = self.clock + self.service_times.pop(0)

    else:  #Server is BUSY
                #increase queue length, this customer will have to wait in the queue
      self.num_in_queue += 1

      #store the arrival time and service time of this customer in seperate lists
      self.times_of_arrivalqueue.append(self.clock)
      self.service_times_in_queue.append(self.service_times.pop(0))
       
       
  def departure1(self):
    if self.num_in_queue == 0:  # if no customer in the queue
      self.server_status1 = 0
      self.next_departure1 = float('inf')

    else:
      self.num_in_queue -= 1
      self.num_of_delays += 1

      last_ind = len(self.times_of_arrivalqueue)

      arrival = self.times_of_arrivalqueue.pop(last_ind - 1)

      last_ind_q = len(self.service_times_in_queue)

      delay = self.clock - arrival
      self.total_delay += delay
      self.next_departure1 = self.clock + self.service_times_in_queue.pop(last_ind_q - 1)

  def departure2(self):
    if self.num_in_queue == 0:  #if no customer in the queue
      self.server_status2 = 0
      self.next_departure2 = float('inf')

    else:
      self.num_in_queue -= 1
      self.num_of_delays += 1

      last_ind = len(self.times_of_arrivalqueue)

      arrival = self.times_of_arrivalqueue.pop(last_ind - 1)

      last_ind_q = len(self.service_times_in_queue)

      delay = self.clock - arrival
      self.total_delay += delay
      self.next_departure2 = self.clock + self.service_times_in_queue.pop(last_ind_q - 1)


  def update_register(self):
    global lifo_ex_no_customers_in_q
    global lifo_ex_uti_s1
    global lifo_ex_uti_s2
    time_differnce = self.clock - self.last_event_time
    self.area_under_qt += self.num_in_queue * time_differnce
    lifo_ex_no_customers_in_q = lifo_ex_no_customers_in_q + self.num_in_queue * time_differnce
    self.area_under_bt1 += self.server_status1 * time_differnce
    lifo_ex_uti_s1 = lifo_ex_uti_s1 + self.server_status1 * time_differnce
    self.area_under_bt2 += self.server_status2 * time_differnce
    lifo_ex_uti_s2 = lifo_ex_uti_s2 + self.server_status2 * time_differnce
    self.last_event_time = self.clock

class sjf:
  def __init__(self):

    self.interarrivals= iat.copy()
    self.service_times= st.copy()
    #print(self.interarrivals)
    #print(self.service_times)
    self.clock = 0.0

    self.next_arrival = self.interarrivals.pop(0)
    self.next_departure1 = float('inf')
    self.next_departure2 = float('inf')

    self.num_in_queue = 0
    self.times_of_arrivalqueue = []  #store times of arrivals who are waiting in the queue
    self.service_times_in_queue = []  #store service times of waiting customers in the queue

    self.total_delay = 0.0
    self.num_of_delays = 0.0
    self.area_under_qt = 0.0
    self.area_under_bt1 = 0.0
    self.area_under_bt2 = 0.0
    self.number_of_customers_in_q = 0.0

    self.server_status1 = 0
    self.server_status2 = 0  #0 for IDLE , 1 for BUSY
    self.last_event_time = 0.0  #we will need to store last event clock time

        
  def start(self):
    while self.num_of_delays <= n:
      self.timing()

  def timing(self):
    self.clock = min(self.next_arrival, self.next_departure1, self.next_departure2)  # First set clock to minimum time of next event
    self.update_register()

    if self.next_arrival < self.next_departure1 and self.next_arrival < self.next_departure2:
      print("Arrival at Clock:" + str(self.clock))
      self.arrival()

    elif self.next_departure1 < self.next_departure2:
      print("Departure of server 1 at " + str(self.clock))
      self.departure1()

    elif self.next_departure2 < self.next_departure1:
      print("Departure of server 2 at " + str(self.clock))
      self.departure2()


    print("Server-1 Status :" + str(self.server_status1))
    print("Server-2 Status :" + str(self.server_status2))
    print("Times of arrivals in Queue: " + str(self.times_of_arrivalqueue))
    print("Service times in Queue: " + str(self.service_times_in_queue))
    print("Number of Delays: " + str(self.num_of_delays))
    print("Total Delay:" + str(self.total_delay))
    print("Area under QT:" + str(self.area_under_qt))
    print("Area under BT1:" + str(self.area_under_bt1))
    print("Area under Bt2:" + str(self.area_under_bt2))
    print("Next Arrival Time: " + str(self.next_arrival))
    print("Next Departure Time of server-1: " + str(self.next_departure1))
    print("Next Departure Time of server-2: " + str(self.next_departure2))
    print("Expected average Delay:" + str(self.total_delay / n))
    self.number_of_customers_in_q = len(self.service_times_in_queue) + self.number_of_customers_in_q
    print("Average number of customers in queue:" + str(self.number_of_customers_in_q / n))
    print("\n--------------------------------------------\n")

    if self.num_of_delays == n:
      global avgd3
      global t3
      avgd3 = self.total_delay
      t3 = self.clock

  def arrival(self):
    self.next_arrival += self.interarrivals.pop(0)

    if self.server_status1 == 0:  #server is idle
      self.server_status1 = 1  #make server BUSY
      delay = 0.0  #so delay is zero
      self.total_delay += delay
      self.num_of_delays += 1  #increase the number of customers delayed

      self.next_departure1 = self.clock + self.service_times.pop(0)

    elif self.server_status2 == 0:  #server is idle
      self.server_status2 = 1  #make server BUSY
      delay = 0.0  #so delay is zero
      self.total_delay += delay
      self.num_of_delays += 1  # increase the number of customers delayed

                #schedule next departure, pop the first element of service_times list to get service time of this customer
      self.next_departure2 = self.clock + self.service_times.pop(0)

    else:  #Server is BUSY
                #increase queue length, this customer will have to wait in the queue
      self.num_in_queue += 1

                #store the arrival time and service time of this customer in seperate lists
      self.times_of_arrivalqueue.append(self.clock)
      self.service_times_in_queue.append(self.service_times.pop(0))
       
       
  def departure1(self):
    if self.num_in_queue == 0:  #if no customer in the queue
      self.server_status1 = 0
      self.next_departure1 = float('inf')

    else:
      self.num_in_queue -= 1
      self.num_of_delays += 1

      index, value = min(enumerate(self.service_times_in_queue), key=operator.itemgetter(1))
      arrival = self.times_of_arrivalqueue.pop(index)

      last_ind_q = len(self.service_times_in_queue)

      delay = self.clock - arrival
      self.total_delay += delay
      self.next_departure1 = self.clock + self.service_times_in_queue.pop(last_ind_q - 1)

  def departure2(self):
    if self.num_in_queue == 0:  #if no customer in the queue
      self.server_status2 = 0
      self.next_departure2 = float('infinity')

    else:
      self.num_in_queue -= 1
      self.num_of_delays += 1

      index, value = min(enumerate(self.service_times_in_queue), key=operator.itemgetter(1))
      arrival = self.times_of_arrivalqueue.pop(index)

      last_ind_q = len(self.service_times_in_queue)
      delay = self.clock - arrival
      self.total_delay += delay
      self.next_departure2 = self.clock + self.service_times_in_queue.pop(last_ind_q - 1)


  def update_register(self):
    global sjf_ex_no_customers_in_q
    global sjf_ex_uti_s1
    global sjf_ex_uti_s2

    time_differnce = self.clock - self.last_event_time
    self.area_under_qt += self.num_in_queue * time_differnce
    sjf_ex_no_customers_in_q = sjf_ex_no_customers_in_q + self.num_in_queue * time_differnce
    self.area_under_bt1 += self.server_status1 * time_differnce
    sjf_ex_uti_s1 = sjf_ex_uti_s1 + self.server_status1 * time_differnce
    self.area_under_bt2 += self.server_status2 * time_differnce
    sjf_ex_uti_s2 = sjf_ex_uti_s2 + self.server_status2 * time_differnce
    self.last_event_time = self.clock



print("Fifo")
fobject = fifo()
fobject.start()
avgd1 = avgd1/n
fifo_ex_no_customers_in_q = fifo_ex_no_customers_in_q/t1
fifo_ex_uti_s1 = fifo_ex_uti_s1/t1
fifo_ex_uti_s2 = fifo_ex_uti_s2/t1
'''print("--------------------------------")
print("Avg Delay(FIFO) :", avgd1 )
print("Expected no of Customers in the Queue :", fifo_ex_no_customers_in_q)
print("Expected Utilization of the Server-1 :", fifo_ex_uti_s1)
print("Expected Utilization of the Server-2 :", fifo_ex_uti_s2)
print("--------------------------------\n\n")'''


print("Lifo")
lobject= lifo()
lobject.start()
avgd2 = avgd2/n
lifo_ex_no_customers_in_q = lifo_ex_no_customers_in_q/t2
lifo_ex_uti_s1 = lifo_ex_uti_s1/t2
lifo_ex_uti_s2 = lifo_ex_uti_s2/t2
'''print("--------------------------------")
print("Avg Delay(LIFO) :", avgd2 )
print("Expected no of Customers in the Queue :", lifo_ex_no_customers_in_q)
print("Expected Utilization of the Server-1 :", lifo_ex_uti_s1)
print("Expected Utilization of the Server-2 :", lifo_ex_uti_s2)
print("--------------------------------\n\n")'''


print("SJF")
sobject= sjf()
sobject.start()
avgd3 = avgd3/n
sjf_ex_no_customers_in_q = lifo_ex_no_customers_in_q/t3
sjf_ex_uti_s1 = lifo_ex_uti_s1/t3
sjf_ex_uti_s2 = lifo_ex_uti_s2/t3

print("--------------------------------")
print("Avg Delay(FIFO) :", avgd1 )
print("Expected no of Customers in the Queue :", fifo_ex_no_customers_in_q)
print("Expected Utilization of the Server-1 :", fifo_ex_uti_s1)
print("Expected Utilization of the Server-2 :", fifo_ex_uti_s2)
print("--------------------------------\n\n")

print("--------------------------------")
print("Avg Delay(LIFO) :", avgd2 )
print("Expected no of Customers in the Queue :", lifo_ex_no_customers_in_q)
print("Expected Utilization of the Server-1 :", lifo_ex_uti_s1)
print("Expected Utilization of the Server-2 :", lifo_ex_uti_s2)
print("--------------------------------\n\n")


print("--------------------------------")
print("Avg Delay(SJF) :", avgd3 )
print("Expected no of Customers in the Queue :", sjf_ex_no_customers_in_q)
print("Expected Utilization of the Server-1 :", sjf_ex_uti_s1)
print("Expected Utilization of the Server-2 :", sjf_ex_uti_s2)
print("--------------------------------\n\n")