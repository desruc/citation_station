import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands

from citation_station.scheduler.jobs.daily_citation import DailyCitationJob


class Scheduler():
    def __init__(self, bot: commands.bot):
        self.scheduler = AsyncIOScheduler()
        self.bot = bot

    def initialize(self):
        self.load_jobs()
        self.start()

    def start(self):
        print("Starting scheduler...")
        self.scheduler.start()
        self.scheduler.print_jobs()  # This is just for debugging

    def load_jobs(self):
        print("Loading jobs...")
        DailyCitationJob(self.bot).schedule(self.scheduler)
