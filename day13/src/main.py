import asyncio

from sync_register import sync_register_paticipants
from async_register import async_register_paticipants, async_register_paticipants_with_delay, \
    async_register_paticipants_with_delay_first, async_register_paticipants_with_delay_as_completed

if __name__ == '__main__':
    #sync_register_paticipants()
    #asyncio.run(async_register_paticipants())
    #asyncio.run(async_register_paticipants_with_delay())
    #asyncio.run(async_register_paticipants_with_delay_first())
    asyncio.run(async_register_paticipants_with_delay_as_completed())
