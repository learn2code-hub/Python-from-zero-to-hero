import asyncio
import time


async def async_register_paticipant(participant_name):
    print(f"Registering {participant_name}...")
    await asyncio.sleep(2)
    print(f"Registration done for {participant_name}")


async def async_register_paticipant_with_delay(participant_name, delay):
    print(f"Registering {participant_name}...")
    await asyncio.sleep(delay)
    print(f"Registration done for {participant_name}")
    return participant_name


async def async_register_paticipants():
    participants = ["John", "Alice", "Bob"]
    start_time = time.time()
    tasks = [async_register_paticipant(participant) for participant in participants]
    await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Total time: {end_time - start_time:.2f}")

async def async_register_paticipants_with_delay():
    participants = [("John", 5), ("Alice", 2), ("Bob", 7)]
    start_time = time.time()
    tasks = [async_register_paticipant_with_delay(*participant) for participant in participants]
    await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Total time: {end_time - start_time:.2f}")


async def async_register_paticipants_with_delay_first():
    participants = [("John", 5), ("Alice", 2), ("Bob", 7)]
    start_time = time.time()
    tasks = [asyncio.create_task(async_register_paticipant_with_delay(*participant)) for participant in participants]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print("Finished tasks:")
    for finished_task in done:
        print(finished_task.result())
    print("Continue registering.....")
    for ongoing_task in pending:
        await ongoing_task

    end_time = time.time()
    print(f"Total time: {end_time - start_time:.2f}")

async def async_register_paticipants_with_delay_as_completed():
    participants = [("John", 5), ("Alice", 2), ("Bob", 7)]
    start_time = time.time()
    tasks = [asyncio.create_task(async_register_paticipant_with_delay(*participant)) for participant in participants]
    for task in asyncio.as_completed(tasks):
        await task
        print(f"Task finished")

    end_time = time.time()
    print(f"Total time: {end_time - start_time:.2f}")