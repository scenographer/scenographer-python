import aiohttp

from scenographer.async_api.core._web_store import WebStore


class ChromeWebStore(WebStore):
    """
    Represents a web store using Chrome Web Store.
    """

    async def download(self, extension_id: str) -> bytes:
        """
        Downloads a WebExtension.

        Parameters
        ----------
        extension_id : str
            The extension identifier.

        Returns
        -------
        bytes
            WebExtension content.
        """

        PROD_VERSION = "49.0"

        url = f"https://clients2.google.com/service/update2/crx" \
            f"?response=redirect" \
            f"&prodversion={PROD_VERSION}" \
            f"&acceptformat=crx3" \
            f"&x=id%3D{extension_id}%26installsource%3Dondemand%26uc"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.content.read()
