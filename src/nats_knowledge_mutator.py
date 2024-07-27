import asyncio
import json
from nats.aio.client import Client as NATS
from typing import Dict, List, Any

class KnowledgeStructure:
    def __init__(self):
        self.data: Dict[str, Any] = {}

    def mutate(self, mutation: Dict[str, Any]):
        # Simple mutation strategy: update or add key-value pairs
        self.data.update(mutation)

class NATSKnowledgeMutator:
    def __init__(self, nats_server: str, subject: str):
        self.nats_server = nats_server
        self.subject = subject
        self.knowledge_structure = KnowledgeStructure()
        self.nc = NATS()

    async def connect(self):
        await self.nc.connect(self.nats_server)

    async def subscribe(self):
        await self.nc.subscribe(self.subject, cb=self.message_handler)

    async def message_handler(self, msg):
        try:
            mutation = json.loads(msg.data.decode())
            self.knowledge_structure.mutate(mutation)
            print(f"Applied mutation: {mutation}")
            print(f"Current knowledge structure: {self.knowledge_structure.data}")
        except json.JSONDecodeError:
            print(f"Invalid JSON received: {msg.data.decode()}")

    async def run(self):
        await self.connect()
        await self.subscribe()
        print(f"Listening for mutations on subject: {self.subject}")
        while True:
            await asyncio.sleep(1)

async def main():
    mutator = NATSKnowledgeMutator("nats://localhost:4222", "nonlocal.info")
    await mutator.run()

if __name__ == "__main__":
    asyncio.run(main())
