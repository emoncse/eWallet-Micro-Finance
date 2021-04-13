rm -rf loan_seeker/migrations
rm -rf investor/migrations
rm -rf central_wallet/migrations
rm -rf loan/migrations
rm -rf user_account/migrations
python manage.py makemigrations loan_seeker
python manage.py migrate loan_seeker
python manage.py makemigrations investor
python manage.py migrate investor
python manage.py makemigrations central_wallet
python manage.py migrate central_wallet
python manage.py makemigrations loan
python manage.py migrate loan
python manage.py makemigrations user_account
python manage.py migrate user_account
python manage.py makemigrations
python manage.py migrate
