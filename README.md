# plugin-privacy

A [Stavrobot](https://github.com/stavrobot) plugin for the [Privacy.com](https://privacy.com) API.

## Tools

### list_transactions

List transactions from your Privacy.com account, with optional filters.

**Parameters** (all optional):

| Name | Type | Description |
|------|------|-------------|
| `account_token` | string | Filter by account UUID |
| `card_token` | string | Filter by card UUID |
| `result` | string | `APPROVED` or `DECLINED` |
| `begin` | string | Include transactions on or after this date (YYYY-MM-DD, inclusive) |
| `end` | string | Include transactions before this date (YYYY-MM-DD, exclusive) |
| `page_size` | integer | Entries per page, 1-1000 (default 50) |
| `page` | integer | Page number, 1+ (default 1) |

## Configuration

After installing the plugin, set your API key in `config.json`:

```json
{
  "api_key": "your-privacy-com-api-key"
}
```

You can generate an API key from your [Privacy.com account page](https://privacy.com/account#api-key). Privacy.com also offers a sandbox environment at `sandbox.privacy.com` with a separate API key.

## License

AGPL-3.0. See [LICENSE](LICENSE).
