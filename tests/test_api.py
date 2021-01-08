# -*- coding: utf-8 -*-
import multiprocessing
import os
from unittest import TestCase

from flask import Flask

from logger.api import app, parse_args


class TestApi(TestCase):

    def setUp(self):
        os.environ["BROKER_URL"] = "http://localhost:5000"
        app = Flask(__name__)
        app.add_url_rule("/", view_func=lambda: "{}", methods=["POST"])
        self.proc = multiprocessing.Process(target=app.run, args=())
        self.proc.start()

    def tearDown(self):
        self.proc.terminate()

    def test_parse_args(self):
        parser = parse_args([])
        self.assertEqual(parser.port, 8080)
        self.assertFalse(parser.enable_cors)

    def test_get(self):
        with app.test_client() as c:
            rv = c.get("/")
            result = rv.get_data(as_text=True)
            expected = "pong"
            self.assertEqual(result, expected)
            self.assertEqual(rv.status_code, 200)

    def test_post(self):
        with app.test_client() as c:
            rv = c.post("/")
            result = rv.get_data(as_text=True)
            self.assertEqual(rv.status_code, 400)

            rv = c.post("/", json={
                "data": {
                    "ndarray": [
                        [1, 2, "a"]
                    ]
                }
            })
            result = rv.get_data(as_text=True)
            self.assertEqual(rv.status_code, 200)

            rv = c.post("/", json={
                "strData": "texto"
            })
            result = rv.get_data(as_text=True)

            rv = c.post("/", json={
                "binData": "Cg=="
            })
            result = rv.get_data(as_text=True)
            self.assertEqual(rv.status_code, 200)

