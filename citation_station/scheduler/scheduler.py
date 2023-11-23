import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands

from citation_station.scheduler.jobs.daily_citation import DailyCitationJob


class Scheduler():
    def __init__(self, bot: commands.bot):
        self.scheduler = AsyncIOScheduler()
        self.bot = bot
        self.job = None

    def initialize(self):
        print("Initializing scheduler...")
        self.cancel_job()
        self.load_job()
        self.start()

    def start(self):
        print("Starting scheduler...")
        if not self.scheduler.running:
            self.scheduler.start()

    def load_job(self):
        print("Loading job...")
        self.job = DailyCitationJob(self.bot).schedule(self.scheduler)

    def cancel_job(self):
        if self.job:
            self.scheduler.remove_job(self.job.id)
            print("Job cancelled.")