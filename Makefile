all: python go


python: .PHONY
	@$(MAKE) -C python generate

go: .PHONY
	@$(MAKE) -C go generate

.PHONY:
