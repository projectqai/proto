package _go

//go:generate sh -c "PATH=\"$(go env GOPATH)/bin:$(go env GOROOT)/bin:$PATH\" protoc --go_out=. --go_opt=paths=source_relative --go-grpc_out=. --go-grpc_opt=paths=source_relative --connect-go_out=. --connect-go_opt=paths=source_relative -I.. ../world.proto"
//go:generate sh -c "PATH=\"$(go env GOPATH)/bin:$(go env GOROOT)/bin:$PATH\" protoc --go_out=. --go_opt=paths=source_relative --go-grpc_out=. --go-grpc_opt=paths=source_relative --connect-go_out=. --connect-go_opt=paths=source_relative -I.. ../timeline.proto"
