import time


def sync_register_participant(participant_name):
    print(f"Registering {participant_name}")
    time.sleep(2)
    print(f"Registration done for {participant_name}")


def sync_register_paticipants():
    participants = ["John", "Alice", "Bob"]
    start_time = time.time()
    for participant in participants:
        sync_register_participant(participant)
    end_time = time.time()
    print(f"Participants registered in {end_time - start_time:.2f} seconds")

