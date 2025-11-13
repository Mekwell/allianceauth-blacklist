Okay, here's an example of what the API looks like now, with the read-only, admin-only access to blacklisted notes.

Remember, you'll need an **admin token** for authentication.

### 1. Get all blacklisted notes

This will return a JSON array containing all `EveNote` objects where `blacklisted` is `True`.

**Request:**
```bash
curl -X GET http://YOUR_ALLIANCE_AUTH_URL/blacklist/api/ -H "Authorization: Token YOUR_ADMIN_TOKEN"
```

**Example JSON Response (truncated for brevity):**
```json
[
    {
        "id": 1,
        "eve_id": 98765432,
        "eve_name": "Example Character One",
        "eve_catagory": "character",
        "blacklisted": true,
        "restricted": false,
        "added_by": "Admin Alpha",
        "added_at": "2025-11-13T12:00:00Z",
        "reason": "Violated code of conduct.",
        "corporation_id": 123456789,
        "corporation_name": "Corp A",
        "alliance_id": 99000001,
        "alliance_name": "Alliance X"
    },
    {
        "id": 2,
        "eve_id": 12345678,
        "eve_name": "Example Corporation Two",
        "eve_catagory": "corporation",
        "blacklisted": true,
        "restricted": true,
        "added_by": "Admin Beta",
        "added_at": "2025-11-12T10:30:00Z",
        "reason": "Known hostile entity.",
        "corporation_id": 12345678,
        "corporation_name": "Example Corporation Two",
        "alliance_id": null,
        "alliance_name": null
    }
]
```

### 2. Get a specific blacklisted note by `eve_id`

This will return a single JSON object for the `EveNote` matching the provided `eve_id`, if it exists and is blacklisted.

**Request:**
```bash
curl -X GET http://YOUR_ALLIANCE_AUTH_URL/blacklist/api/98765432/ -H "Authorization: Token YOUR_ADMIN_TOKEN"
```

**Example JSON Response:**
```json
{
    "id": 1,
    "eve_id": 98765432,
    "eve_name": "Example Character One",
    "eve_catagory": "character",
    "blacklisted": true,
    "restricted": false,
    "added_by": "Admin Alpha",
    "added_at": "2025-11-13T12:00:00Z",
    "reason": "Violated code of conduct.",
    "corporation_id": 123456789,
    "corporation_name": "Corp A",
    "alliance_id": 99000001,
    "alliance_name": "Alliance X"
}
```

If the `eve_id` does not exist or the corresponding note is not blacklisted, you would receive a `404 Not Found` response.
