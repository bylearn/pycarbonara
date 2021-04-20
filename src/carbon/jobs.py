import asyncio
import base64
import sys

from pyppeteer import launch


async def get_content(url):
    browser = await launch(
        headless=True,
        executablePath="/usr/bin/chromium-browser",
        args=["--no-sandbox", "--disable-gpu"],
    )
    page = await browser.newPage()
    await page.goto(url)
    await page.setViewport(
        {
            "width": 8192,
            "height": 2048,
            "deviceScaleFactor": 2,
        }
    )

    await page.evaluate(
        """() => {
    document.querySelector("html").style.background = "none";
    document.querySelector("body").style.background = "none";
    document.querySelector(".editor").style.background = "none";
    document.querySelector(".alpha").style.background = "none";
    document.querySelector(".white").style.background = "none";
    }"""
    )

    element = await page.querySelector("#export-container  .container-bg")

    image = await element.screenshot({"omitBackground": True})

    await browser.close()

    print(base64.b64encode(image))


url = sys.argv[1]

asyncio.get_event_loop().run_until_complete(get_content(url))
