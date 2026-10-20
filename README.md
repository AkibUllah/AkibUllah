<!-- topics: portfolio, profile -->
# Hi, I'm Akib Jafor

Senior Full-Stack Engineer in Dhaka, Bangladesh. Six-plus years shipping production systems in FinTech, cloud infrastructure, AgriTech and retail. I build the whole product: Python backends (FastAPI, Django), React / Next.js / Vue frontends in TypeScript, and the Docker, nginx and OpenStack infrastructure underneath.

- Currently: Sr. Software Engineer at GenNext Technologies, building **Meghna Cloud**, an OpenStack-based cloud platform for Bangladesh.
- Before that: payment gateways and billing/settlement for mobile financial services and banks, a KYC onboarding system for a bank's mobile app, and AWD irrigation monitoring tools for Japanese agricultural consultants.
- Portfolio site: https://akibullah.github.io/portfolio

## What I work with

| Area | Tools |
|---|---|
| Backend | Python, FastAPI, Django, Django REST Framework, SQLAlchemy, Pydantic, GraphQL (Strawberry) |
| Frontend | TypeScript, React, Next.js, Vue 3, Tailwind CSS, TanStack Query, Zustand, Pinia |
| Data | PostgreSQL, MySQL, Redis, SQLite, DuckDB, pandas, scikit-learn |
| Infra | Docker, docker compose, nginx, GitHub Actions, OpenStack, Linux |
| Domains | Payments (bKash, SSLCommerz, Stripe), billing and settlement, KYC, e-commerce and POS, cloud metering, AgriTech |

## Projects

Every repository below is a complete, runnable project with tests, a Dockerfile and CI. They are grouped by the kind of work they demonstrate.

### FinTech and payments

| Repo | What it is |
|---|---|
| [fastapi-payment-gateway](https://github.com/AkibUllah/fastapi-payment-gateway) | Multi-provider payment gateway with a payment state machine, idempotency keys, HMAC-signed webhooks, routing by fee table, settlement and reconciliation. |
| [billing-settlement-engine](https://github.com/AkibUllah/billing-settlement-engine) | Django + DRF double-entry ledger, tiered fee schedules, invoicing and partner settlement batches with CSV reconciliation. |
| [bkash-python-sdk](https://github.com/AkibUllah/bkash-python-sdk) | Typed sync/async Python client for bKash Tokenized Checkout with retries, token refresh and webhook helpers. |
| [webhook-relay](https://github.com/AkibUllah/webhook-relay) | Reliable webhook delivery service: exponential backoff, signatures, circuit breakers, dead-letter queue and replay. |
| [kyc-onboarding-api](https://github.com/AkibUllah/kyc-onboarding-api) | KYC onboarding workflow with document validation, NID checks, risk scoring, reviewer roles and SLA tracking. |

### Cloud platform and backend infrastructure

| Repo | What it is |
|---|---|
| [cloud-usage-metering](https://github.com/AkibUllah/cloud-usage-metering) | Usage ingestion, rating engine with tiered pricing and proration, invoices and budget alerts for cloud resources. |
| [multi-tenant-saas-auth](https://github.com/AkibUllah/multi-tenant-saas-auth) | Multi-tenant auth service: rotating refresh tokens, RBAC, org-scoped API keys, invitations and rate limiting. |
| [rate-limiter-service](https://github.com/AkibUllah/rate-limiter-service) | Token bucket, sliding window and GCRA limiters with in-memory and Redis (Lua) backends, plus FastAPI middleware and benchmarks. |
| [openstack-resource-manager](https://github.com/AkibUllah/openstack-resource-manager) | CLI to inventory, audit and cost-estimate OpenStack resources, with a fake cloud client for tests. |
| [realtime-monitoring-dashboard](https://github.com/AkibUllah/realtime-monitoring-dashboard) | FastAPI WebSocket metrics stream with alert rules and a React live dashboard. |
| [docker-fastapi-react-template](https://github.com/AkibUllah/docker-fastapi-react-template) | Production starter: async FastAPI + Alembic + Postgres + Redis, React frontend, nginx, compose for dev and prod, CI and deploy workflow. |
| [log-analytics-pipeline](https://github.com/AkibUllah/log-analytics-pipeline) | Nginx log parsing, path normalisation, percentiles and anomaly detection into DuckDB, with CLI and HTML reports. |
| [url-shortener-analytics](https://github.com/AkibUllah/url-shortener-analytics) | URL shortener with expiry, QR codes, Redis-cached redirects and click analytics. |

### E-commerce, retail and bookings

| Repo | What it is |
|---|---|
| [ecommerce-api](https://github.com/AkibUllah/ecommerce-api) | Django REST e-commerce backend: catalog, carts, stock reservation, coupons, bKash/COD checkout and delivery zones. |
| [nextjs-ecommerce-storefront](https://github.com/AkibUllah/nextjs-ecommerce-storefront) | Next.js 14 App Router storefront with ISR, cart, checkout server actions and English/Bangla i18n. |
| [pos-offline-first](https://github.com/AkibUllah/pos-offline-first) | Offline-first PWA point of sale with IndexedDB, outbox sync and a FastAPI sync server. |
| [appointment-booking-system](https://github.com/AkibUllah/appointment-booking-system) | Doctor appointment booking with timezone-aware slot generation, double-booking protection and reminders. |
| [inventory-forecasting](https://github.com/AkibUllah/inventory-forecasting) | Demand forecasting and reorder-point toolkit for retail POS data with backtesting. |

### Frontend engineering

| Repo | What it is |
|---|---|
| [react-admin-dashboard](https://github.com/AkibUllah/react-admin-dashboard) | React + TypeScript admin dashboard with TanStack Query, Zustand, Recharts, forms and a mocked API layer. |
| [react-form-builder](https://github.com/AkibUllah/react-form-builder) | Drag-and-drop form builder that exports JSON Schema and renders forms with zod validation. |
| [vue-cloud-console](https://github.com/AkibUllah/vue-cloud-console) | Vue 3 + Pinia cloud console UI: instance wizard, volumes, security groups, billing. |
| [bangla-i18n-toolkit](https://github.com/AkibUllah/bangla-i18n-toolkit) | Zero-dependency TypeScript library for Bangla numerals, BDT formatting, dates and phone validation. |

### AgriTech and reusable libraries

| Repo | What it is |
|---|---|
| [agri-field-monitor](https://github.com/AkibUllah/agri-field-monitor) | AWD irrigation monitoring backend with GraphQL API, field geometry, water-level alerts and progress reports. |
| [django-audit-log](https://github.com/AkibUllah/django-audit-log) | Reusable Django app for field-level audit trails with masking, request context and pruning. |

## Contact

- Portfolio: https://akibullah.github.io/portfolio
- GitHub: https://github.com/AkibUllah
