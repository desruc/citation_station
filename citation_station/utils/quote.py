import aiohttp
from aiohttp import ClientSession
import random

zen_quotes_url = "https://zenquotes.io/api/today"
quotable_url = "https://api.quotable.io/random"

async def fetch(session: ClientSession, url: str):
    async with session.get(url) as response:
        return await response.json()

async def get_zen_qoute():
    async with aiohttp.ClientSession() as session:
        response = await fetch(session, zen_quotes_url)
        quote = response[0].get("q")
        author = response[0].get("a")
        return [quote, author]

async def get_quotable_quote():
    async with aiohttp.ClientSession() as session:
        response = await fetch(session, quotable_url)
        quote = response.get("content")
        author = response.get("author")
        return [quote, author]

async def get_quote():
    quote_funcs = [get_zen_qoute, get_quotable_quote]
    quote = await random.choice(quote_funcs)()
    return quote