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
event state handling would flood the terminal with endless data instead of the specific historical data

Lessons learned: Make a habbit of adding documention and making git commits

Next session: complete event state tranisiton


2026-09-09

GOal: complete implementation of improved event state transition

completed: added new_status, and previous_status(also properly used previous_status over previous_health_status so data will show the correct state needed) (Later date change prevous_health_status to hold persistant health status rather than hard coded "normal" in)


lessons learned: Learned the value of testing and implemented new iterations. test for bugs and get it working, then implemenet an optimized way with seperation of concerns to keep clean code and create code that works and can be scaled. 


Next session: Add an operators dashboard




2026-09-16

Goal: Add an operator Dashboard

Completed: Added a basic operator dashboard to be used for the actual web-based dashboard

Next Session: add a system summary to optimise what operators see so only the most important information is shown in proper order of severity.

Lesson learned: Frequent testing at ever section of the project can allow you to fix formatting errors and create the best project possible, The more errors you fix before you get to the end product means a more optimized and precise project.



2026-09-17

Goal: create a new operator dasboard and add a dashboard health to display the actual health status of the transformer

Completed: Added display_operator_dashboard and rearranged where the display call is located within while true loop to bottom of the loop. created a dictionary for dashboard_health to allow the dictionary to be populated the analyzed by the display operator dashboard. added asset_id and health to the def display dashboard function to allow equiptment health to be viewed.

lessons learned: Understanding placement of code in a systems mindset to troubleshoot errors in code that might not be shown in the terminal as an error but rather the feautre did not meet the sharholder requirements. The more I work with code the more the patterns make themselves known.

Next session: Add an overall system status to the operator display

2026-09-21

Goal: Add an overall system status to operator display and active alarm section

Completed: Added an overall system status to view total amount of events.

Lessons learned:Adding a counter and linking that coutner to display_health which contains the collected events needed, can give an operator dashboard a cleaner and more effective way at looking at problems that need to be addressed. Adding an active alarm system allows the dashboard to be even cleaner by keeping alarms up until they are cleared instwad on constatly filling the dashboard with events.  .values() only gives the value of a dictionary, while .items() gives the key and value of that dictionary (Side note: .keys() return only the key)

Next session: