---
name: smz-event
description: "Generates the 3-tier email dispatch schedule for Still Mind Zendo (SMZ) events, retreats, study programs (Ango), discussion circles (Thursday Circle), Work Practice Morning, Week Sesshin, Focusing workshops, ceremonies, and all zendo closures within a 2-month window from either a user-specified start date or the current date using the embedded annual calendar. Use when the user asks to calculate email announcement dates from a specific date, membership mailing timelines, retreat notice schedules, Thursday Circle announcements, Ango registration timelines, Work Practice Morning notices, Week Sesshin schedules, Focusing workshop dates, or zendo closed notifications for SMZ."
---
# SMZ Event Cadence

Calculates and outputs the standard 3-tier email announcement schedule for upcoming Still Mind Zendo events, retreats, study periods, discussion circles, Work Practice Morning, Week Sesshin, Focusing workshops, ceremonies, and zendo closures across a rolling 2-month lookahead window starting from a user-specified date (or defaulting to the current date if unspecified).

## When to Use

  - Planning email campaigns from a specific reference date (e.g., "starting November 1", "from January 2027", or today).
  - Scheduling member announcements for all Zendo closures and schedule changes.
  - Planning retreats (Zazenkai, Sesshin, Week Sesshin, Silence-in-the-City).
  - Planning workshops (Focusing Workshop).
  - Scheduling ceremonies and special meetings (Annual Sangha Meeting, Jukai Ceremony, Rohatsu Celebration).
  - Scheduling Work Practice Morning sessions (specifically 10/31/26 and 3/27/27).
  - Scheduling Thursday Night Circle reflection/discussion announcements and Zoom links.
  - Managing registration and study timelines for Ango (intensive practice period).

## Embedded Reference Calendar: SMZ 2026-2027

Below is the verified calendar of events from `SMZ_2026_2027.xlsx` (excluding Intro to Zen):

| Date | Day | Event / Category | Notes |
| :--- | :--- | :--- | :--- |
| **09/01/2026** | Tuesday | **Zendo Opens** | Fall season begins |
| **09/17/2026** | Thursday | **Thursday Circle** | 7:00 PM – 8:30 PM (Members only) |
| **09/19/2026** | Saturday | **Zazenkai** | 8:55 AM – 5:30 PM ($25 members / $50 non-members) |
| **10/06/2026** | Tuesday | **Annual Sangha Meeting** | Community business & elections |
| **10/17/2026** | Saturday | **Zazenkai** | 8:55 AM – 5:30 PM ($25 members / $50 non-members) |
| **10/29/2026** | Thursday | **Jukai Ceremony** | Precepts ceremony |
| **10/31/2026** | Saturday | **Work Practice Morning** | Samu & community lunch (Strict date 1 of 2) |
| **11/05/2026** | Thursday | **Thursday Circle** | 7:00 PM – 8:30 PM (Members only) |
| **11/13/2026 – 11/15/2026** | Fri – Sun | **Weekend Sesshin (Mariandale #1)** | Residential ($300 members / $375 non-members) |
| **11/26/2026 – 11/28/2026** | Thu – Sat | **Zendo Closed (Thanksgiving)** | Closed through weekend |
| **12/01/2026 – 12/15/2026** | Tue – Tue | **Rohatsu Practice Period** | Two-week intensive sitting |
| **12/11/2026 – 12/12/2026** | Fri – Sat | **Winter Silence in the City (Rohatsu)** | Fri 6:55 PM – 9:00 PM; Sat 8:30 AM – 5:30 PM |
| **12/15/2026** | Tuesday | **Rohatsu Sangha Celebration / End** | Conclusion of Rohatsu period |
| **12/21/2026 – 01/04/2027** | Mon – Mon | **Zendo Closed (Winter Holidays)** | Reopens Jan 5, 2027 |
| **01/14/2027** | Thursday | **Thursday Circle** | 7:00 PM – 8:30 PM (Members only) |
| **01/16/2027** | Saturday | **Zazenkai** | 8:55 AM – 5:30 PM ($25 members / $50 non-members) |
| **02/02/2027** | Tuesday | **Ango Start** | 6-week intensive practice period ($120 fee, members only) |
| **02/04/2027** | Thursday | **Ango Study** | Weekly Thursday evening study |
| **02/11/2027** | Thursday | **Ango Study** | Weekly Thursday evening study |
| **02/12/2027 – 02/14/2027** | Fri – Sun | **Weekend Sesshin (Mariandale #2)** | Residential ($300 members / $375 non-members) |
| **02/18/2027** | Thursday | **Ango Study** | Weekly Thursday evening study |
| **02/25/2027** | Thursday | **Ango Study** | Weekly Thursday evening study |
| **03/04/2027** | Thursday | **Ango Study** | Weekly Thursday evening study |
| **03/11/2027** | Thursday | **Ango Study** | Weekly Thursday evening study |
| **03/13/2027** | Saturday | **Zazenkai** | 8:55 AM – 5:30 PM ($25 members / $50 non-members) |
| **03/16/2027** | Tuesday | **Ango End** | Conclusion of Ango |
| **03/20/2027** | Saturday | **Focusing Workshop** | Experiential Somatic Zen workshop |
| **03/27/2027** | Saturday | **Work Practice Morning** | Samu & community lunch (Strict date 2 of 2) |
| **04/09/2027 – 04/10/2027** | Fri – Sat | **Spring Silence in the City (Buddha's Birthday)** | Fri 6:55 PM – 9:00 PM; Sat 8:30 AM – 5:30 PM |
| **04/15/2027** | Thursday | **Thursday Circle** | 7:00 PM – 8:30 PM (Members only) |
| **05/08/2027** | Saturday | **Zazenkai** | 8:55 AM – 5:30 PM ($25 members / $50 non-members) |
| **05/13/2027** | Thursday | **Thursday Circle** | 7:00 PM – 8:30 PM (Members only) |
| **05/29/2027 – 05/31/2027** | Sat – Mon | **Zendo Closed (Memorial Day Weekend)** | Holiday closure |
| **06/06/2027 – 06/12/2027** | Sun – Sat | **Week Sesshin (Seven Meadows Farm #1)** | Residential ($550, members only) |
| **06/20/2027 – 06/26/2027** | Sun – Sat | **Week Sesshin (Seven Meadows Farm #2)** | Residential ($550, members only) |
| **07/03/2027 – 07/05/2027** | Sat – Mon | **Zendo Closed (July 4th Weekend)** | Holiday closure |

*(Note: Intro to Zen events are excluded from scheduled email cadence dispatches).*

## The 3-Tier Dispatch Patterns by Event Type

### 1. Zendo Closed / Facility Closures & Recesses

  - **Tier 1 (Advance Notice)**: 21 to 22 days prior (~3 weeks out). Advance notice in weekly sangha communications detailing affected sittings.
  - **Tier 2 (Mid-Cycle Reminder)**: 10 to 12 days prior (~1.5 weeks out). Reinforces specific canceled sitting dates and clarifies the last sitting prior to closure.
  - **Tier 3 (Final Week-Of Notice)**: 3 to 4 days prior. Dedicated closure notice issued right before the last regular sitting, confirming exact dates closed and reopening sitting date/time.

### 2. Retreats (Zazenkai, Weekend Sesshin, Silence-in-the-City)

  - **Tier 1 (Initial Announcement)**: 21 to 24 days prior (or ~4 weeks before registration cutoff for residential sesshins). Full details, schedule, fees, and registration link.
  - **Tier 2 (Mid-Cycle Reminder)**: 10 to 12 days prior (or ~10 days before registration cutoff). Progress check, seat availability, reminder of requirements.
  - **Tier 3 (Final Call / Approaching Deadline)**: 3 to 4 days prior (or 2 to 3 days before the registration deadline). Final reminder and payment cutoff notice.

### 3. Week Sesshin (Seven Meadows Farm Extended Residential)

  - **Tier 1 (Initial Announcement & Registration Opening)**: 5 to 6 weeks prior (~35 to 42 days out). Comprehensive announcement with lodging options, full schedule, teacher interviews, dana, and scholarship/work exchange options.
  - **Tier 2 (Mid-Cycle / Housing Cutoff Reminder)**: 3 weeks prior (~21 days out). Focuses on approaching housing deadlines, dietary requests, and seat capacity.
  - **Tier 3 (Final Preparation & Logistics Briefing)**: 7 to 10 days prior (or ~3 days before final registration cutoff). Detailed logistics, packing guidelines, ride shares, orientation time, and roster finalization.

### 4. Focusing Workshop

  - **Tier 1 (Workshop Announcement & Registration Open)**: 24 to 28 days prior (~4 weeks out). Introduces teacher/facilitator, somatic methodology, workshop schedule, fee, and registration cutoff.
  - **Tier 2 (Mid-Cycle Reminder & Participant Cap Check)**: 12 to 14 days prior (~2 weeks out). Highlights remaining spaces, preparation notes, and registration progress.
  - **Tier 3 (Final Call & Preparation Materials)**: 4 to 5 days prior (or ~2 days before registration deadline). Distributes schedule details, Zoom credentials (if hybrid/online), or in-person arrival logistics.

### 5. Work Practice Morning (Scheduled strictly on 10/31/26 and 03/27/27)

  - **Tier 1 (Save-the-Date & Task Overview)**: 21 to 24 days prior (~3 weeks out). Outlines project areas (altar care, cushion maintenance, library, kitchen, repairs) and RSVP request for lunch headcount.
  - **Tier 2 (Mid-Cycle Call for Volunteers)**: 10 to 12 days prior. Details schedule (morning work block followed by informal sangha lunch), specific needs, and confirms coordinator contacts.
  - **Tier 3 (Week-Of Logistics & RSVP Confirmation)**: 3 to 4 days prior. Final confirmation of arrival instructions, lunch headcount, and weather-dependent plans if outdoor work is involved.

### 6. Ceremonies & Meetings (Annual Sangha Meeting, Jukai, Rohatsu Celebration)

  - **Tier 1 (Event Announcement & Agenda/Theme)**: 21 to 24 days prior (~3 weeks out). Formal notification of event date, purpose, agenda/precepts context, and attendance protocol.
  - **Tier 2 (Mid-Cycle Reminder & Participation Details)**: 10 to 12 days prior. Confirms schedule, coordinator points of contact, and RSVP/potluck or reception coordination.
  - **Tier 3 (Final Week-Of Notice)**: 3 to 4 days prior. Logistics, in-person arrival time, and Zoom link (for hybrid meetings).

### 7. Thursday Night Circle

  - **Tier 1 (Initial Topic & Prompt Announcement)**: 24 days prior (~3.5 weeks out, typically Monday). Shares topic, reflection questions, leaders, and format.
  - **Tier 2 (Mid-Cycle Reflection Reminder)**: 10 to 12 days prior (Monday/Tuesday). Re-shares contemplative prompt and questions.
  - **Tier 3 (Week-Of Notice & Zoom Link)**: 2 to 3 days prior (Monday/Tuesday week of event). Final reminder with Zoom link for long-distance students.

### 8. Ango (Intensive Practice Period)

  - **Tier 1 (Program Announcement & Registration Open)**: 4 to 5 weeks prior to Ango start (early January). Explains theme, syllabus, weekly Thursday schedule, fee ($120), and registration link.
  - **Tier 2 (Mid-Cycle / Commitment Reminder)**: 2 weeks prior (~14 days before start). Encourages enrollment and outlines preparatory readings.
  - **Tier 3 (Final Call / Roster Finalization)**: 4 to 5 days prior to Opening Ceremony. Distributes initial readings and study zoom credentials to registered participants.

## Step-by-Step Procedure

1. **Establish the Reference Start Date**:
   - Parse the prompt for any user-specified date (e.g., "starting December 1, 2026", "from Jan 15", "for March 2027").
   - If no start date is stated, default to the current execution date.
   - Establish the 2-month (60-day) window as `[Start Date] to [Start Date + 60 days]`.
2. **Query the Calendar**: Extract all events from the embedded reference calendar falling within the 60-day window (skipping Intro to Zen).
3. **Calculate Dispatch Timelines**: Compute Tier 1, Tier 2, and Tier 3 dispatch dates using the event-specific lead times.
4. **Evaluate Status Relative to Start Date**:
   - Mark an item as "Due" if the target date equals or directly precedes the reference start date.
   - Mark as "Upcoming" if it falls after the reference start date.
   - Mark as "Completed" if it is well before the reference start date.
5. **Format Output**: Deliver a structured Markdown table sorted chronologically by event date.
