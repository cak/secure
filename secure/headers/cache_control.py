from typing import List


class CacheControl:
    """
    Prevent cacheable HTTPS response

    Resources:
    https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control
    """

    def __init__(self) -> None:
        self.__policy: List[str] = []
        self.header = "Cache-Control"
        self.value = "no-store"

    def _build(self, directive: str) -> None:
        self.__policy.append(directive)
        self.value = ", ".join(self.__policy)

    def set(self, value: str) -> "CacheControl":
        """Set custom value for `Cache-control` header

        :param value: custom header value
        :type value: str
        :return: CacheControl class
        :rtype: CacheControl
        """
        self._build(value)
        return self

    def immutable(self) -> "CacheControl":
        self._build("immutable")
        return self

    def max_age(self, seconds: int) -> "CacheControl":
        self._build(f"max-age={seconds}")
        return self

    def max_stale(self, seconds: int) -> "CacheControl":
        self._build(f"max-stale={seconds}")
        return self

    def min_fresh(self, seconds: int) -> "CacheControl":
        self._build(f"min-fresh={seconds}")
        return self

    def must_revalidate(self) -> "CacheControl":
        self._build("must-revalidate")
        return self

    def no_cache(self) -> "CacheControl":
        self._build("no-cache")
        return self

    def no_store(self) -> "CacheControl":
        self._build("no-store")
        return self

    def no_transform(self) -> "CacheControl":
        self._build("no-transform")
        return self

    def only_if_cached(self) -> "CacheControl":
        self._build("only-if-cached")
        return self

    def private(self) -> "CacheControl":
        self._build("private")
        return self

    def proxy_revalidate(self) -> "CacheControl":
        self._build("proxy-revalidate")
        return self

    def public(self) -> "CacheControl":
        self._build("public")
        return self

    def s_maxage(self, seconds: int) -> "CacheControl":
        self._build(f"s-maxage={seconds}")
        return self

    def stale_if_error(self, seconds: int) -> "CacheControl":
        self._build(f"stale-if-error={seconds}")
        return self

    def stale_while_revalidate(self, seconds: int) -> "CacheControl":
        self._build(f"stale-while-revalidate={seconds}")
        return self