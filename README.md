# AuthScore

**Minimal Email Authentication Scorer for Solo Founders**

Signature: Mourad.Soltani

A small, shippable CLI tool that scores your domain's SPF and DMARC configuration (0-100) and suggests concrete fixes. Inspired by the trending "inbox-authentication fix kit" micro-SaaS niche (2026).

## Why this?

Small businesses lose deliverability and face spoofing risk from missing or weak SPF/DMARC. This tool gives an instant score + action list. No SaaS login, no subscription — just run it.

## Quick start

```bash
python authscore.py example.com
python authscore.py example.com --json
```

## Health tests

```bash
python -m unittest tests.test_health -v
```

All tests must pass.

## Roadmap (micro-SaaS)

- Real DNS resolution (dnspython)
- DKIM selector probing
- One-click record generation
- Simple web UI + Stripe for monitoring

## License

MIT — see LICENSE

Built by Mourad.Soltani as a solo product experiment.
