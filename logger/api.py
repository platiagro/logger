# -*- coding: utf-8 -*-
"""WSGI server."""
import argparse
import sys

from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, NotFound, MethodNotAllowed, \
    Forbidden, InternalServerError

from logger.controller import create_log

app = Flask(__name__)


@app.route("/", methods=["GET"])
def ping():
    """
    Handles GET requests to /.
    """
    return "pong"


@app.route("/", methods=["POST"])
def post_logs():
    """
    Handles POST requests to /.
    """
    body = request.get_json(force=True)
    create_log(body)
    return jsonify(body)


@app.errorhandler(BadRequest)
@app.errorhandler(NotFound)
@app.errorhandler(MethodNotAllowed)
@app.errorhandler(Forbidden)
@app.errorhandler(InternalServerError)
def handle_errors(e):
    """Handles exceptions raised by the API."""
    return jsonify({"message": e.description}), e.code


def parse_args(args):
    """Takes argv and parses API options."""
    parser = argparse.ArgumentParser(
        description="Logger API"
    )
    parser.add_argument(
        "--port", type=int, default=8080, help="Port for HTTP server (default: 8080)",
    )
    parser.add_argument("--enable-cors", action="count")
    parser.add_argument(
        "--debug", action="count", help="Enable debug",
    )
    return parser.parse_args(args)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])

    # Enable CORS if required
    if args.enable_cors:
        CORS(app)

    app.run(host="0.0.0.0", port=args.port, debug=args.debug)
