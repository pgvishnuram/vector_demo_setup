.DEFAULT_GOAL := help

.PHONY: help
help: ## Print Makefile help.
	@grep -Eh '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-41s\033[0m %s\n", $$1, $$2}'


.PHONY: install-es 
install-es: ## Install ElasticSearch Service
	docker-compose up -d

.PHONY: cleanup-es 
cleanup-es: ## Cleanup ElasticSearch Service
	docker-compose down -v