all: python go ts


python: .PHONY
	@$(MAKE) -C python generate

go: .PHONY
	@$(MAKE) -C go generate

ts: .PHONY
	@$(MAKE) -C ts generate

.PHONY:
