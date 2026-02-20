# Mining Operations Management - Odoo 17 Custom Module

![Odoo Version](https://img.shields.io/badge/Odoo-17.0-blue)
![License](https://img.shields.io/badge/License-LGPL--3-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

## Overview
A custom Odoo 17 ERP module designed for **mining industry operations management**. This module provides comprehensive tools to manage mining sites, heavy equipment, and daily production records.

## Features
- **Mining Site Management** — Track multiple mining sites with location, mineral type, area, and operational status
- **Heavy Equipment Tracking** — Monitor excavators, dump trucks, bulldozers, and other equipment with maintenance schedules
- **Daily Production Recording** — Record shift-based production with target vs actual volume tracking
- **Achievement Monitoring** — Automatic calculation of production achievement percentage
- **Audit Trail** — Full activity log and chatter on every record

## Module Structure
```
mining_operations/
├── models/
│   ├── mining_site.py        # Mining site model
│   ├── heavy_equipment.py    # Heavy equipment model
│   └── daily_production.py   # Daily production model
├── views/
│   ├── mining_site_views.xml
│   ├── heavy_equipment_views.xml
│   ├── daily_production_views.xml
│   └── menu_views.xml
├── security/
│   └── ir.model.access.csv
├── __manifest__.py
└── __init__.py
```

## Installation

### Prerequisites
- Odoo 17.0
- Python 3.10+
- PostgreSQL 15+

### Via Docker (Recommended)
```bash
git clone https://github.com/USERNAME/odoo-mining-operations.git
cd odoo-mining-operations
docker-compose up -d
```

### Manual Installation
1. Copy the `mining_operations` folder to your Odoo addons directory
2. Restart Odoo server
3. Enable Developer Mode
4. Go to Apps > Update Apps List
5. Search for "Mining Operations" and click Install

## Dependencies
- base
- mail
- hr (Employees)
- maintenance

## Models

### mining.site
| Field | Type | Description |
|-------|------|-------------|
| name | Char | Site name |
| code | Char | Site code |
| mineral_type | Selection | Coal, Gold, Nickel, Tin, Copper, Bauxite |
| location | Char | Site location |
| area_hectare | Float | Area in hectares |
| status | Selection | Active, Inactive, Under Maintenance |
| responsible_id | Many2one | Site manager (hr.employee) |

### heavy.equipment
| Field | Type | Description |
|-------|------|-------------|
| name | Char | Equipment name |
| equipment_type | Selection | Excavator, Dump Truck, Bulldozer, etc |
| site_id | Many2one | Assigned mining site |
| operator_id | Many2one | Equipment operator |
| status | Selection | Operational, Maintenance, Breakdown, Standby |

### daily.production
| Field | Type | Description |
|-------|------|-------------|
| date | Date | Production date |
| site_id | Many2one | Mining site |
| shift | Selection | Morning, Afternoon, Night |
| volume_target | Float | Target volume (tons) |
| volume_actual | Float | Actual volume (tons) |
| achievement | Float | Auto-calculated achievement % |

## Author
**Bryan Frisco Peraira**
- GitHub: [@bryanfrisco](https://github.com/bryanfrisco)
- Website: [Web Portfolio](https://bryanfrisco.github.io)

## License
LGPL-3
