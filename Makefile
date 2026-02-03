all: fmt python go ts


fmt:
	buf format -w

python: .PHONY
	@$(MAKE) -C python generate

go: .PHONY
	@$(MAKE) -C go generate

ts: .PHONY
	@$(MAKE) -C ts generate

.PHONY:
