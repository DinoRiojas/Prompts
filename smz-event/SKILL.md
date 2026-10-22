---
name: smz-event
description: Generates the 3-tier email dispatch schedule for Still Mind Zendo (SMZ) events, retreats, study programs (Ango), discussion circles (Thursday Circle), Work Practice Morning, Week Sesshin, Focusing workshops, ceremonies, and zendo closures across a rolling 2-month window (or for a specified date range) using the verified SMZ 2026-2027 Tier Schedule spreadsheet as the authoritative basis. Use when the user asks to calculate email announcement dates, membership mailing timelines, retreat notice schedules, Thursday Circle announcements, Ango registration timelines, Work Practice Morning notices, Week Sesshin schedules, Focusing workshop dates, or zendo closed notifications for SMZ.
---
# SMZ Event Cadence

Generates and outputs the standard 3-tier email announcement schedule for Still Mind Zendo (SMZ) events, retreats, study periods, discussion circles, Work Practice Morning, Week Sesshin, Focusing workshops, ceremonies, and zendo closures across a rolling 2-month lookahead window starting from a user-specified reference date (defaulting strictly to today's date if unspecified).

The outputs are strictly grounded in the verified master schedule from `SMZ_TIER_2026_2027_Populated.xlsx` / `SMZ_TIER_2026_2027.xlsx`, which forms the deterministic basis for all Tier 1, Tier 2, and Tier 3 dispatch dates.

## When to Use

- Planning email campaigns from a specific reference date or defaulting to today's date when unspecified.
- Scheduling member announcements for all Zendo closures and schedule changes.
- Planning retreats (Zazenkai, Sesshin, Week Sesshin, Silence-in-the-City).
- Planning workshops (Focusing Workshop).
- Scheduling ceremonies and special meetings (Annual Sangha Meeting, Jukai Ceremony, Rohatsu Celebration).
- Scheduling Work Practice Morning sessions (specifically 10/31/2026 and 03/27/2027).
- Scheduling Thursday Night Circle reflection/discussion announcements and Zoom links.
- Managing registration and study timelines for Ango (intensive practice period).

## Master Spreadsheet Reference Schedule (SMZ 2026–2027)

Below is the verified master dispatch schedule constructed in `SMZ_TIER_2026_2027_Populated.xlsx`. This table serves as the primary source of truth for all email tier dates (excluding Intro to Zen):

| Event Date(s) | Day(s) | Event / Program Name | Tier 1 Dispatch (Initial / Open) | Tier 2 Dispatch (Mid-Cycle) | Tier 3 Dispatch (Final / Logistics) | Category & Operational Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **09/01/2026** | Tuesday | **Zendo Opens** | 08/10/2026 – 08/11/2026 | 08/20/2026 – 08/22/2026 | 08/28/2026 – 08/29/2026 | Fall season begins; weekly schedule resumes |
| **09/17/2026** | Thursday | **Thursday Circle** | 08/24/2026 | 09/05/2026 – 09/07/2026 | 09/14/2026 – 09/15/2026 | 7:00 PM – 8:30 PM (Members only) |
| **09/19/2026** | Saturday | **Zazenkai** | 08/26/2026 – 08/29/2026 | 09/07/2026 – 09/09/2026 | 09/15/2026 – 09/16/2026 | 8:55 AM – 5:30 PM ($25 members / $50 non-members) |
| **10/06/2026** | Tuesday | **Annual Sangha Meeting** | 09/12/2026 – 09/15/2026 | 09/24/2026 – 09/26/2026 | 10/02/2026 – 10/03/2026 | Community business meeting & elections |
| **10/17/2026** | Saturday | **Zazenkai** | 09/23/2026 – 09/26/2026 | 10/05/2026 – 10/07/2026 | 10/13/2026 – 10/14/2026 | 8:55 AM – 5:30 PM ($25 members / $50 non-members) |
| **10/29/2026** | Thursday | **Jukai Ceremony** | 10/05/2026 – 10/08/2026 | 10/17/2026 – 10/19/2026 | 10/25/2026 – 10/26/2026 | Precepts ceremony protocol |
| **10/31/2026** | Saturday | **Work Practice Morning** | 10/07/2026 – 10/10/2026 | 10/19/2026 – 10/21/2026 | 10/27/2026 – 10/28/2026 | Samu & community lunch (Date 1 of 2) |
| **11/05/2026** | Thursday | **Thursday Circle** | 10/12/2026 | 10/24/2026 – 10/26/2026 | 11/02/2026 – 11/03/2026 | 7:00 PM – 8:30 PM (Members only) |
| **11/13/2026 – 11/15/2026** | Fri – Sun | **Weekend Sesshin (Mariandale #1)** | 10/01/2026 | 10/15/2026 | 10/20/2026 | Residential ($300 members / $375 non-members) |
| **11/26/2026 – 11/28/2026** | Thu – Sat | **Zendo Closed (Thanksgiving)** | 11/04/2026 – 11/05/2026 | 11/14/2026 – 11/16/2026 | 11/22/2026 – 11/23/2026 | Holiday closure through Saturday |
| **12/01/2026 – 12/15/2026** | Tue – Tue | **Rohatsu Practice Period** | 11/07/2026 – 11/10/2026 | 11/19/2026 – 11/21/2026 | 11/26/2026 – 11/27/2026 | Two-week intensive sitting period |
| **12/11/2026 – 12/12/2026** | Fri – Sat | **Winter Silence in the City (Rohatsu)** | 11/17/2026 – 11/20/2026 | 11/29/2026 – 12/01/2026 | 12/07/2026 – 12/08/2026 | Fri 6:55 PM – 9:00 PM; Sat 8:30 AM – 5:30 PM |
| **12/15/2026** | Tuesday | **Rohatsu Sangha Celebration / End** | 11/21/2026 – 11/24/2026 | 12/03/2026 – 12/05/2026 | 12/11/2026 – 12/12/2026 | Rohatsu conclusion & sangha potluck |
| **12/21/2026 – 01/04/2027** | Mon – Mon | **Zendo Closed (Winter Holidays)** | 11/29/2026 – 11/30/2026 | 12/09/2026 – 12/11/2026 | 12/17/2026 – 12/18/2026 | Winter recess; reopens Jan 5, 2027 |
| **01/14/2027** | Thursday | **Thursday Circle** | 12/21/2026 | 01/02/2027 – 01/04/2027 | 01/11/2027 – 01/12/2027 | 7:00 PM – 8:30 PM (Members only) |
| **01/16/2027** | Saturday | **Zazenkai** | 12/23/2026 – 12/26/2026 | 01/04/2027 – 01/06/2027 | 01/12/2027 – 01/13/2027 | 8:55 AM – 5:30 PM ($25 members / $50 non-members) |
| **02/02/2027** | Tuesday | **Ango Start** | 12/29/2026 – 01/05/2027 | 01/19/2027 | 01/28/2027 – 01/29/2027 | 6-week intensive practice period ($120 fee, members only) |
| **02/04/2027** | Thursday | **Ango Study** | — | — | — | Weekly study covered under Ango registration |
| **02/11/2027** | Thursday | **Ango Study** | — | — | — | Weekly study covered under Ango registration |
| **02/12/2027 – 02/14/2027** | Fri – Sun | **Weekend Sesshin (Mariandale #2)** | 01/01/2027 | 01/15/2027 | 01/20/2027 | Residential ($300 members / $375 non-members) |
| **02/18/2027** | Thursday | **Ango Study** | — | — | — | Weekly study covered under Ango registration |
| **02/25/2027** | Thursday | **Ango Study** | — | — | — | Weekly study covered under Ango registration |
| **03/04/2027** | Thursday | **Ango Study** | — | — | — | Weekly study covered under Ango registration |
| **03/11/2027** | Thursday | **Ango Study** | — | — | — | Weekly study covered under Ango registration |
| **03/13/2027** | Saturday | **Zazenkai** | 02/17/2027 – 02/20/2027 | 03/01/2027 – 03/03/2027 | 03/09/2027 – 03/10/2027 | 8:55 AM – 5:30 PM ($25 members / $50 non-members) |
| **03/16/2027** | Tuesday | **Ango End** | — | — | — | Conclusion of Ango practice period |
| **03/20/2027** | Saturday | **Focusing Workshop** | 02/20/2027 – 02/24/2027 | 03/06/2027 – 03/08/2027 | 03/15/2027 – 03/16/2027 | Experiential Somatic Zen workshop |
| **03/27/2027** | Saturday | **Work Practice Morning** | 03/03/2027 – 03/06/2027 | 03/15/2027 – 03/17/2027 | 03/23/2027 – 03/24/2027 | Samu & community lunch (Date 2 of 2) |
| **04/09/2027 – 04/10/2027** | Fri – Sat | **Spring Silence in the City (Buddha's Birthday)** | 03/16/2027 – 03/19/2027 | 03/28/2027 – 03/30/2027 | 04/05/2027 – 04/06/2027 | Fri 6:55 PM – 9:00 PM; Sat 8:30 AM – 5:30 PM |
| **04/15/2027** | Thursday | **Thursday Circle** | 03/22/2027 | 04/03/2027 – 04/05/2027 | 04/12/2027 – 04/13/2027 | 7:00 PM – 8:30 PM (Members only) |
| **05/08/2027** | Saturday | **Zazenkai** | 04/14/2027 – 04/17/2027 | 04/26/2027 – 04/28/2027 | 05/04/2027 – 05/05/2027 | 8:55 AM – 5:30 PM ($25 members / $50 non-members) |
| **05/13/2027** | Thursday | **Thursday Circle** | 04/19/2027 | 05/01/2027 – 05/03/2027 | 05/10/2027 – 05/11/2027 | 7:00 PM – 8:30 PM (Members only) |
| **05/29/2027 – 05/31/2027** | Sat – Mon | **Zendo Closed (Memorial Day Weekend)** | 05/07/2027 – 05/08/2027 | 05/17/2027 – 05/19/2027 | 05/25/2027 – 05/26/2027 | Holiday closure through Monday |
| **06/06/2027 – 06/12/2027** | Sun – Sat | **Week Sesshin (Seven Meadows Farm #1)** | 05/01/2027 | 05/15/2027 | 05/20/2027 | Residential ($550, members only) |
| **06/20/2027 – 06/26/2027** | Sun – Sat | **Week Sesshin (Seven Meadows Farm #2)** | 05/01/2027 | 05/15/2027 | 05/20/2027 | Residential ($550, members only) |
| **07/03/2027 – 07/05/2027** | Sat – Mon | **Zendo Closed (July 4th Weekend)** | 06/11/2027 – 06/12/2027 | 06/21/2027 – 06/23/2027 | 06/29/2027 – 06/30/2027 | Holiday closure through Monday |

*(Note: All Intro to Zen events, weekly Ango Study sessions, and multi-day end rows are marked as `—` because they do not have separate automated email tier dispatches).*

## The 3-Tier Dispatch Patterns

1. **Zendo Closed / Facility Closures & Recesses**:
   - **Tier 1 (Advance Notice)**: 21 to 22 days prior (~3 weeks out). Advance notice in weekly sangha communications detailing affected sittings.
   - **Tier 2 (Mid-Cycle Reminder)**: 10 to 12 days prior (~1.5 weeks out). Reinforces specific canceled sitting dates and clarifies last sitting prior to closure.
   - **Tier 3 (Final Week-Of Notice)**: 3 to 4 days prior. Dedicated closure notice issued right before the last regular sitting, confirming reopening date/time.

2. **Weekend Sesshin (Residential at Mariandale)**:
   - **Tier 1 (Initial Announcement & Registration Open)**: 1st day of the previous calendar month before the retreat (Oct 1 for Nov Sesshin; Jan 1 for Feb Sesshin).
   - **Tier 2 (Mid-Cycle Reminder & Seat Check)**: 15th day of the previous calendar month before the retreat (Oct 15 for Nov Sesshin; Jan 15 for Feb Sesshin).
   - **Tier 3 (Final Call & Payment / Registration Deadline)**: 20th day of the previous calendar month before the retreat (Oct 20 for Nov Sesshin; Jan 20 for Feb Sesshin).

3. **Week Sesshin (Seven Meadows Farm Extended Residential)**:
   - **Tier 1 (Initial Announcement & Registration Opening)**: 1st day of the previous calendar month before the retreat (May 1 for June Sesshin #1 and #2).
   - **Tier 2 (Mid-Cycle Reminder & Seat / Housing Check)**: 15th day of the previous calendar month before the retreat (May 15 for June Sesshin #1 and #2).
   - **Tier 3 (Final Call & Payment / Registration Deadline)**: 20th day of the previous calendar month before the retreat (May 20 for June Sesshin #1 and #2).

4. **Other Retreats (Zazenkai, Silence-in-the-City)**:
   - **Tier 1 (Initial Announcement)**: 21 to 24 days prior (~4 weeks before registration cutoff). Full details, schedule, fees, and registration link.
   - **Tier 2 (Mid-Cycle Reminder)**: 10 to 12 days prior (~10 days before registration cutoff). Seat availability, reminder of requirements.
   - **Tier 3 (Final Call / Approaching Deadline)**: 3 to 4 days prior (~2 to 3 days before deadline). Final reminder and payment cutoff notice.

5. **Focusing Workshop**:
   - **Tier 1 (Workshop Announcement & Registration Open)**: 24 to 28 days prior (~4 weeks out). Introduces facilitator, somatic methodology, schedule, fee, and cutoff.
   - **Tier 2 (Mid-Cycle Reminder & Participant Cap Check)**: 12 to 14 days prior (~2 weeks out). Remaining spaces, preparation notes, and registration progress.
   - **Tier 3 (Final Call & Preparation Materials)**: 4 to 5 days prior (or ~2 days before registration deadline). Schedule details, Zoom credentials, or arrival logistics.

6. **Work Practice Morning (10/31/2026 and 03/27/2027)**:
   - **Tier 1 (Save-the-Date & Task Overview)**: 21 to 24 days prior (~3 weeks out). Outlines project areas (altar care, cushion maintenance, library, repairs) and lunch headcount RSVP.
   - **Tier 2 (Mid-Cycle Call for Volunteers)**: 10 to 12 days prior. Details schedule (morning work block followed by informal sangha lunch) and confirms coordinator contacts.
   - **Tier 3 (Week-Of Logistics & RSVP Confirmation)**: 3 to 4 days prior. Final confirmation of arrival instructions, lunch headcount, and weather-dependent plans.

7. **Ceremonies & Meetings (Annual Sangha Meeting, Jukai, Rohatsu Celebration)**:
   - **Tier 1 (Event Announcement & Agenda/Theme)**: 21 to 24 days prior (~3 weeks out). Formal notification of event date, purpose, agenda/precepts context, and attendance protocol.
   - **Tier 2 (Mid-Cycle Reminder & Participation Details)**: 10 to 12 days prior. Confirms schedule, coordinator points of contact, and RSVP/potluck coordination.
   - **Tier 3 (Final Week-Of Notice)**: 3 to 4 days prior. Logistics, in-person arrival time, and Zoom link (for hybrid meetings).

8. **Thursday Night Circle**:
   - **Tier 1 (Initial Topic & Prompt Announcement)**: 24 days prior (~3.5 weeks out, typically Monday). Shares topic, reflection questions, leaders, and format.
   - **Tier 2 (Mid-Cycle Reflection Reminder)**: 10 to 12 days prior (Monday/Tuesday). Re-shares contemplative prompt and questions.
   - **Tier 3 (Week-Of Notice & Zoom Link)**: 2 to 3 days prior (Monday/Tuesday week of event). Final reminder with Zoom link for long-distance students.

9. **Ango (Intensive Practice Period)**:
   - **Tier 1 (Program Announcement & Registration Open)**: 4 to 5 weeks prior to Ango start (early January). Explains theme, syllabus, weekly Thursday schedule, fee ($120), and registration link.
   - **Tier 2 (Mid-Cycle / Commitment Reminder)**: 2 weeks prior (~14 days before start). Encourages enrollment and outlines preparatory readings.
   - **Tier 3 (Final Call / Roster Finalization)**: 4 to 5 days prior to Opening Ceremony. Distributes initial readings and study zoom credentials to registered participants.

## Step-by-Step Execution Procedure

1. **Establish the Reference Start Date**:
   - Parse the prompt for any user-specified date (e.g., "starting December 1, 2026", "from Jan 15", "for March 2027").
   - **Defaulting Rule**: If no start date is specified in the prompt, explicitly use today's date as the reference start date.
   - Establish the rolling 2-month (60-day) window as `[Start Date] to [Start Date + 60 days]`.

2. **Query the Master Spreadsheet Calendar**:
   - Extract all events from the Master Spreadsheet Reference Schedule whose event date falls within the 60-day window (skipping Intro to Zen and multi-day end dates).

3. **Populate Tier Dispatch Timelines Directly from Spreadsheet Basis**:
   - Take the pre-calculated Tier 1, Tier 2, and Tier 3 dispatch windows directly from the Master Spreadsheet Reference Schedule table above. Do not guess or re-invent dates.

4. **Evaluate Status Relative to Reference Start Date**:
   - Compare each Tier dispatch date/window against the reference start date:
     - **Completed**: The dispatch window has already ended prior to the reference start date.
     - **Due / Active**: The dispatch window is currently open, encompasses today's date, or falls within the immediate 48-hour window.
     - **Upcoming**: The dispatch window is in the future relative to the reference start date.

5. **Format Output**:
   - Deliver a clean Markdown table sorted chronologically by event date, including:
     - `Event Date`
     - `Event / Category`
     - `Tier 1 (Initial / Advance)`
     - `Tier 2 (Mid-Cycle Reminder)`
     - `Tier 3 (Final Notice / Logistics)`
     - `Current Status & Action Required`
