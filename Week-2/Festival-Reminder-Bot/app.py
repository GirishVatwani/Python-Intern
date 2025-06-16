from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta, time
from plyer import notification
from time import sleep

EVENT = dict()

#Initializers
#Scheduler
scheduler = BackgroundScheduler()
# Add a persistent job store
scheduler.add_jobstore(SQLAlchemyJobStore(url='sqlite:///jobs.sqlite'))

def event_manager(title, event_datetime):
    if title in EVENT.keys():
        EVENT[title] = event_datetime
    else:
        EVENT[title] = event_datetime

def notify_user(title = "Notification", text = 'Test Notification'):
    notification.notify(
        title=title,
        message=text,
        app_name="Festival Reminder",
        timeout=5 )

def create_job(title, description, event_datetime):
    try:
        scheduler.add_job(notify_user, 'date', run_date=event_datetime, args=[title, description], replace_existing=True)
        print(f"Job scheduled for {event_datetime} with title '{title}' and description '{description}'")
    except Exception as e:
        print("Error scheduling job:", e)

def test_job(hrs=0, mits=0, sec=60):
    current_datetime = datetime.now()
    margine = timedelta(hours=hrs, minutes=mits, seconds=sec)
    datetime_obj = current_datetime + margine

    scheduler.add_job(notify_user, 'date', run_date=datetime_obj, args=["Test Job", "This is to test the App"])
    print("This is a test job running at", datetime.now())
    notify_user("Test Job", "This is a test notification from the Festival Reminder Bot.")
    print(f"Current Date & Time: {current_datetime} \nScheduled Date & Time: {datetime_obj}")
    return datetime_obj

def get_datetime():
    Date = input("Enter Date (DD/MM/YYYY): ")
    Time = input("Enter Time (HH:MM): ")
    return datetime.strptime(f"{Date} {Time}", "%d/%m/%Y %H:%M")

def get_event_details():
    title = input("Enter Event Title: ")
    description = input("Enter Event Description: ")
    event_datetime = get_datetime()
    return title, description, event_datetime

def get_choice():
    print("\n\n1. Create a new event")
    print("2. Show existing events")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice not in ['1', '2', "3", "000"]:
        print("Invalid choice. Please try again.")
        return get_choice()
    return choice

def main(largest_datetime=datetime.now()):
    choice = get_choice()
    if choice == '1':
        title, description, event_datetime = get_event_details()

        # Validate the event date and time
        if event_datetime > largest_datetime:
            largest_datetime = event_datetime
        create_job(title, description, event_datetime)
        EVENT[title] = event_datetime

        # Start the scheduler
        scheduler.start()
        print("Scheduler started. Waiting for the job to execute...")
        main(largest_datetime)


    elif choice == '2':
        print("Note: The Event Manager Don't store the description, " \
        "but the description will be visible on the notification and the events are not editable" \
        "Because the events are stored by the external secured databases\n")

        print("Existing Events:")
        if not EVENT:
            print("No events scheduled. You may exit safely")
            main()
        for title, event_datetime in EVENT.items():
            print(f"{title} - {event_datetime}")
        main()

    elif choice == "3":
        if scheduler.running:
            #Ask to stop the scheduler
            stop_scheduler = input("Do you want to stop the scheduler? (yes/no): ").strip().lower()
        elif stop_scheduler == "yes":
            scheduler.shutdown()
            print("Scheduler stopped.")
        else:
            print("Scheduler is still running in the background.")
            while datetime.now() < largest_datetime:
                sleep(1)
                if not scheduler.running:
                    print("Scheduler has been stopped.")
                    exit()
            exit()

    elif choice == "000":
        print("Welcome to the Bot Settings")
        #Under Development
        print("This feature is in under development, please try again later.")
        main()
    else:
        print("Invalid choice. Please try again.")
        main()


if __name__ == "__main__":
    print("Welcome to the Festival Reminder Bot!")
    main()



