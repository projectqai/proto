#!/usr/bin/env python3
"""
Example usage of platform-proto Python bindings.

This demonstrates how to use the generated protobuf classes.
"""

import logging
import grpc
from google.protobuf import timestamp_pb2
from platform_proto import timeline_pb2, timeline_pb2_grpc
from platform_proto import world_pb2, world_pb2_grpc

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def timeline_example():
    """Example of using the Timeline service."""
    logger.info("=== Timeline Service Example ===\n")

    # Create a GetTimelineRequest
    get_request = timeline_pb2.GetTimelineRequest()
    logger.info(f"GetTimelineRequest: {get_request}")

    # Create a MoveTimelineRequest
    move_request = timeline_pb2.MoveTimelineRequest()
    move_request.freeze = True

    # Set timestamp
    now = timestamp_pb2.Timestamp()
    now.GetCurrentTime()
    move_request.at.CopyFrom(now)

    logger.info(f"MoveTimelineRequest: {move_request}")


def world_example():
    """Example of using the World service."""
    logger.info("=== World Service Example ===\n")

    # Create a ListEntitiesRequest
    list_request = world_pb2.ListEntitiesRequest()
    logger.info(f"ListEntitiesRequest: {list_request}")

    # Create a GetEntityRequest
    get_request = world_pb2.GetEntityRequest()
    get_request.id = "entity-123"
    logger.info(f"GetEntityRequest: {get_request}")

    # Create an Entity
    entity = world_pb2.Entity()
    entity.id = "test-entity-001"

    # Set up geospatial component
    entity.geo.longitude = -73.935242
    entity.geo.latitude = 40.730610
    entity.geo.altitude = 10.0

    # Set up symbol component
    entity.symbol.milStd2525C = "SFGPUCI-------"

    logger.info(f"Entity: {entity}")


def grpc_client_example(server_address='localhost:50051'):
    """
    Example of connecting to a gRPC server.

    Note: This will fail if no server is running at the specified address.
    """
    logger.info("=== gRPC Client Example ===\n")
    logger.info(f"Attempting to connect to {server_address}...")

    try:
        # Create a channel
        channel = grpc.insecure_channel(server_address)

        # Create stubs
        timeline_stub = timeline_pb2_grpc.TimelineServiceStub(channel)

        # Example: Call GetTimeline
        request = timeline_pb2.GetTimelineRequest()

        # Set a timeout to avoid hanging
        response = timeline_stub.GetTimeline(request, timeout=5.0)

        logger.info(f"Timeline response: {response}")

    except grpc.RpcError as e:
        logger.error(f"gRPC Error: {e.code()} - {e.details()}")
    except Exception as e:
        logger.warning(f"Connection failed: {e}")
        logger.info("(This is expected if no server is running)")


def main():
    """Run all examples."""
    logger.info("Platform Proto - Python Bindings Examples")
    logger.info("=" * 50)

    # Show message creation examples
    timeline_example()
    world_example()

    # Optionally try to connect to a server
    # Uncomment the next line if you have a server running
    # grpc_client_example()

    logger.info("=" * 50)
    logger.info("Examples complete!")


if __name__ == "__main__":
    main()
