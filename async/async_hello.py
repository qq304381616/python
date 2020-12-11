#!/usr/bin/env python3
# -*- coding: utf-8 -*-


""" 异步任务 """

import asyncio
import threading


async def hello(name):
    print('Hello world! (%s)(%s)' % (name, threading.currentThread()))
    await asyncio.sleep(2)
    print('Hello again! (%s)(%s)' % (name, threading.currentThread()))


loop = asyncio.get_event_loop()
tasks = [hello("name1"), hello("name2")]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
