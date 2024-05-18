# Security header recommendations and information from the MDN Web Docs and the OWASP Secure Headers Project
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Embedder-Policy
# https://owasp.org/www-project-secure-headers/#cross-origin-embedder-policy
#
# Cross-Origin-Embedder-Policy by Mozilla Contributors is licensed under CC-BY-SA 2.5.
# https://developer.mozilla.org/en-US/docs/MDN/Community/Roles_teams#contributor
# https://creativecommons.org/licenses/by-sa/2.5/


class CrossOriginEmbedderPolicy:
    """
    The Cross-Origin-Embedder-Policy (COEP) header prevents a document from loading any cross-origin resources
    that don’t explicitly grant the document permission

    - CORP applies on the loaded resource side (resource owner)
    - COEP applies on the “loader” of the resource side (consumer of the resource).

    Resources:
    https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Opener-Policy
    https://owasp.org/www-project-secure-headers/#cross-origin-embedder-policy
    """

    def __init__(self) -> None:
        self.header = "Cross-Origin-Embedder-Policy"
        self.value = "require-corp"

    def set(self, value: str) -> "CrossOriginEmbedderPolicy":
        """Set custom value for Cross-Origin-Opener-Policy header

        :param value: custom header value
        :type value: str
        :return: CrossOriginEmbedderPolicy class
        :rtype: CrossOriginEmbedderPolicy
        """
        self.value = value
        return self

    def unsafe_none(self) -> "CrossOriginEmbedderPolicy":
        """Allows the document to fetch cross-origin resources without giving explicit permission through
        the CORS protocol or the Cross-Origin-Resource-Policy header (it is the default value).

        https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Opener-Policy
        https://owasp.org/www-project-secure-headers/#cross-origin-embedder-policy

        :return: CrossOriginEmbedderPolicy class
        :rtype: CrossOriginEmbedderPolicy
        """
        self.value = "unsafe-none"
        return self

    def require_corp(self) -> "CrossOriginEmbedderPolicy":
        """A document can only load resources from the same origin,
        or resources explicitly marked as loadable from another origin.

        https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Opener-Policy
        https://owasp.org/www-project-secure-headers/#cross-origin-embedder-policy

        :return: CrossOriginEmbedderPolicy class
        :rtype: CrossOriginEmbedderPolicy
        """
        self.value = "require-corp"
        return self