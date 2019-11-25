import threading, time

def intro():
    print("Start of program.")

    def take_a_nap():
        time.sleep(5)
        print("WAKE UP")

    thread_obj = threading.Thread(target=take_a_nap)
    thread_obj.start()
    print("End of program.")

def passing_arguments():
    thr = threading.Thread(target=print, args=['cats', 'dogs', 'frogs'], kwargs={'sep': ' & '})
    thr.start()

passing_arguments()
