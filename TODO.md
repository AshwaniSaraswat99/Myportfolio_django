# Deployment Setup Tasks

- [x] Move all contents from `myportfolio/` subdirectory to repository root
- [x] Update `manage.py` to set `DJANGO_SETTINGS_MODULE` to "myportfolio.settings"
- [x] Remove duplicate `requirements.txt` from old `myportfolio/` location
- [x] Verify paths in `settings.py` are correct after move
- [x] Test project locally with `python manage.py runserver`
- [x] Run `python manage.py collectstatic` to collect static files
- [x] Run `python manage.py migrate` if deploying to a new database
- [ ] Commit changes and deploy to platform (e.g., Render)
