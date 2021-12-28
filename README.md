# Test Blockchain
Quick sample test repository to represent how a block chain is built and provide a sample console application to Demo the Blockchain for a user.

- _Note: only create a singular blockchain, for multiple "coins" there would need to be multiple chains_

# Console Application
The console application is runnable via Python 3 and a set of possible commands to help demo what is occurring

### Commands
- Transaction (T): 
    - Record a new transaction on the blockchain

- Mine (M):
    - Commit the mining operation to start mining available transactions in order to create a new block on the chain

- Print (P):
    - Print out the current state of the block chain

- Quit (Q):
    - Close the simulation


### Sample
Below is a sample of a computed block chain with a difficulty of 5
```JSON
{
    "chain": [
        {
            "hash": "a50bd955c0b6dd2c4c74eb47cfb42b1a8b7b6c6e0ebf96b7c84486ab8d0037ac",
            "identifier": "33d5db25-417b-4d36-bbde-a298cf43375b",
            "nonce": 0,
            "previous_hash": "",
            "timestamp": 1640669612.6042135,
            "transactions": []
        },
        {
            "hash": "00000206e2cfda00c7b5ef02d8bd1e33975d77450a211384f6c1a0da411a65be",
            "identifier": "256c0b7d-27b7-43a4-a596-ed5be4ca8603",
            "nonce": 821072,
            "previous_hash": "a50bd955c0b6dd2c4c74eb47cfb42b1a8b7b6c6e0ebf96b7c84486ab8d0037ac",
            "timestamp": 1640669614.996363,
            "transactions": [
                "76c52265-ef2a-4fa5-bffe-8e111b5437ae",
                "8960c6d9-a543-4d39-aeb1-5a26e7982745"
            ]
        },
        {
            "hash": "00000c1cfe330a1291219acbca1417e47c0e551ec45929c985e70a86a56b4eda",
            "identifier": "7425ba2c-13c4-4a8c-9329-4a57044dd112",
            "nonce": 2371131,
            "previous_hash": "00000206e2cfda00c7b5ef02d8bd1e33975d77450a211384f6c1a0da411a65be",
            "timestamp": 1640669626.1871605,
            "transactions": [
                "d7071de3-998b-4f85-a169-217b07a0efdf",
                "ff1915f3-1d22-4e3c-840e-75bd24a4bec5"
            ]
        },
        {
            "hash": "0000008e05ae64cb5db3f7d884ac9e61ee0422f48fe8b4b7384ab11a43f01ec9",
            "identifier": "f97c7c41-b7d8-46b8-87ec-407e16bda1c7",
            "nonce": 428058,
            "previous_hash": "00000c1cfe330a1291219acbca1417e47c0e551ec45929c985e70a86a56b4eda",
            "timestamp": 1640669654.749287,
            "transactions": [
                "fa3897f1-6773-4f75-bb1d-2045d06f80ec",
                "fb359b14-83a1-40ca-a2df-2b9cd3cd579a",
                "1ed65ffe-3492-4fb0-b159-87614d75507b",
                "452a3ddd-39e5-46f8-a0f2-1d4eaab5177b",
                "405ca882-473a-4c75-8f10-4d19506294e8"
            ]
        }
    ],
    "difficulty": 5,
    "waiting_transactions": [
        "25ca0339-360a-4021-ad1a-648b97ce1f0e",
        "e0b38b87-2e7c-4f94-9468-6c6740de7b92"
    ]
}
```