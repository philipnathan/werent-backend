#!/bin/sh

echo "Waiting for MySQL..."


check_mysql() {
    mysqladmin ping -h "$MYSQL_HOST" -P "$MYSQL_PORT" -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" > /dev/null 2>&1
}

sleep 10

until check_mysql; do
    >&2 echo "MySQL is unavailable - sleeping"
    sleep 3
done

echo "MySQL started"

export FLASK_APP=run.py
export FLASK_ENV=${FLASK_ENV}

cd /backend
flask db init
flask db migrate
flask db upgrade
python seed_data.py
python run.py