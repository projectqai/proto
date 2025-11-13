#!/usr/bin/env python3
"""
Example usage of platform-proto Python bindings.

This demonstrates how to use the generated protobuf classes.
"""

import grpc
from google.protobuf import timestamp_pb2
from platform_proto import timeline_pb2, timeline_pb2_grpc
from platform_proto import world_pb2, world_pb2_grpc


def timeline_example():
    """Example of using the Timeline service."""
    print("=== Timeline Service Example ===\n")

    # Create a GetTimelineRequest
    get_request = timeline_pb2.GetTimelineRequest()
    print(f"GetTimelineRequest: {get_request}")

    # Create a MoveTimelineRequest
    move_request = timeline_pb2.MoveTimelineRequest()
    move_request.freeze = True

    # Set timestamp
    now = timestamp_pb2.Timestamp()
    now.GetCurrentTime()
    move_request.at.CopyFrom(now)

    print(f"MoveTimelineRequest: {move_request}")
    print()


def world_example():
    """Example of using the World service."""
    print("=== World Service Example ===\n")

    # Create a ListEntitiesRequest
    list_request = world_pb2.ListEntitiesRequest()
    print(f"ListEntitiesRequest: {list_request}")

    # Create a GetEntityRequest
    get_request = world_pb2.GetEntityRequest()
    get_request.id = "entity-123"
    print(f"GetEntityRequest: {get_request}")

    # Create an Entity
    entity = world_pb2.Entity()
    entity.id = "test-entity-001"

    # Set up geospatial component
    entity.geo.longitude = -73.935242
    entity.geo.latitude = 40.730610
    entity.geo.altitude = 10.0

    # Set up symbol component
    entity.symbol.milStd2525C = "SFGPUCI-------"

    print(f"Entity: {entity}")
    print()


def grpc_client_example(server_address='localhost:50051'):
    """
    Example of connecting to a gRPC server.

    Note: This will fail if no server is running at the specified address.
    """
    print(f"=== gRPC Client Example ===\n")
    print(f"Attempting to connect to {server_address}...")

    try:
        # Create a channel
        channel = grpc.insecure_channel(server_address)

        # Create stubs
        timeline_stub = timeline_pb2_grpc.TimelineServiceStub(channel)

        # Example: Call GetTimeline
        request = timeline_pb2.GetTimelineRequest()

        # Set a timeout to avoid hanging
        response = timeline_stub.GetTimeline(request, timeout=5.0)

        print(f"Timeline response: {response}")

    except grpc.RpcError as e:
        print(f"gRPC Error: {e.code()} - {e.details()}")
    except Exception as e:
        print(f"Connection failed: {e}")
        print("(This is expected if no server is running)")

    print()


def main():
    """Run all examples."""
    print("Platform Proto - Python Bindings Examples")
    print("=" * 50)
    print()

    # Show message creation examples
    timeline_example()
    world_example()

    # Optionally try to connect to a server
    # Uncomment the next line if you have a server running
    # grpc_client_example()

    print("=" * 50)
    print("Examples complete!")


if __name__ == "__main__":
    main()
