2026-08-05

Goal: Add multi-transformer support

Completed: 
- Converted Transformer object to transformer list
- added TX-101, TX-102, TX-103
- updated telemetry collection loops for list alteration

Issues: 
- Health report only displayed tx-103 
    Root cause was due to indentation outside of loop. and old code that only showed the last transformer

Next session: 
- improve event state transitions


2026-09-05

Goal: Improve event state transitions and add documentation '

Completed:
- Added decisions,engineering,roadmap, and architecture.md(s) 
-

Issues: Started documentation today so most changes have to be remembered and added at future date

Lessons learned: Make a habbit of adding documention and making git commits

Next session: complete event state tranisiton


2026-09-09

GOal: complete implementation of improved event state transition

completed: added new_status, and previous_status(also properly used previous_status over previous_health_status so data will show the correct state needed) (Later date change prevous_health_status to hold persistant health status rather than hard coded "normal" in)

Next session: Add an operators dashboard
