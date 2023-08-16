#!/bin/sh

T=$(date +"%d.%m.%Y-%H:%M:%S")

alembic revision --autogenerate -m "$T"
