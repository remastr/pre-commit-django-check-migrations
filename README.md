# pre-commit hook to check whether django migrations were created

This hook is meant to be used with [pre-commit](https://github.com/pre-commit/pre-commit).

## Usage

To your `.pre-commit-config.yaml` add hook config similar to this:

``` yaml
repos:
    -   repo: https://github.com/remastr/pre-commit-django-check-migrations
        rev: v0.1.0
        hooks:
        -   id: check-migrations-created
            args: [--exec-command=poetry run python, --manage-path=sample_project/manage.py]
```

## Hook arguments

| Argument | Description | Default value |
| --- | --- | --- |
| `--exec-command` | Command to execute manage.py with (can be set to run in docker container, poetry shell, etc.) | python3 |
| `--manage-path` | Path to manage.py file | ./src/manage.py |

## Additional dependencies

If you opt not to use hook in docker environment / virtual environment with django installed,
you need to add django to `additional_dependencies` of the hook:

``` yaml
repos:
    -   repo: https://github.com/remastr/pre-commit-django-check-migrations
        rev: v0.1.0
        hooks:
        -   id: check-migrations-created
            args: [--manage-path=sample_project/manage.py]
            additional_dependencies: [
                django==3.2.1
            ]
```
