from flask import Flask, request

from src.metasearch.service import MetaSearchService


class Server(Flask):
    def __init__(self, name: str, metasearch: MetaSearchService):
        super().__init__(name)
        self._metasearch = metasearch
        urls = [
            ('/search', self.search, {}),
        ]
        for url in urls:
            if len(url) == 3:
                self.add_url_rule(url[0], url[1].__name__, url[1], **url[2])

    def search(self):
        text = request.args.get('text')
        user_id = request.args.get('user_id')
        ip = request.args.get('ip_addr')
        if ip is None:
            ip = request.remote_addr
        return self._metasearch.search(text, user_id, ip)

    def run_server(self, **kwargs):
        super().run(host='0.0.0.0', port=8000, **kwargs)
