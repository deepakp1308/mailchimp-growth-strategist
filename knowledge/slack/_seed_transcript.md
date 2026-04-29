# Slack Transcript: Aug 1, 2025 - Apr 28, 2026

Source channels:
- `#mailchimp-launched` (C03TLJNADSP) - launches & customer impact
- `#mc-experimentation-xfn` (C095TT75VTQ) - cross-team experiment alignment, weekly Tuesday sync

Pulled: 2026-04-28. Top-level messages only (chronological, oldest first).

---

# CHANNEL: #mailchimp-launched

**125 top-level messages**

---

=== Message from Chima Okechukwu (U03AME5740K) at 2025-08-01 09:47:52 PDT === 
Message TS: 1754066872.212719
_*#SHIP IT:*_ :green-light-siren::green-light-siren:

:rocket-launch::rocket-launch:  *Launched Escape Hatch for GSSO Customers* :rocket-launch: :rocket-launch: 

:emailintensifies:*Executive Summary*
On 05/18, the team noticed a significant drop in Account Setup completion rate after the launch of the GSSO experience. Going deeper into customer VOCs, we discovered that existing customers were "stuck" on the Profile Step in Account Setup with no way to log out. That was because in the GSSO experience, these customers were being misclassified as new customers, so were taken to the Account Setup flow. So, these customers saw Account Setup instead of the Homepage like they normally would. This drove multiple VOCs like these:

_"LET ME OUT -- I did not use the correct name to sign in and it will not remove me so I can use the correct name and password."_ 
"_It's impossible to log out! Stop being so annoying!!!!!_"
_More VOCs_: <https://docs.google.com/spreadsheets/d/1EtXhAndpFxPiPsud7lGCIFrfBrpCMMMroSyYhnI5ycA/edit?gid=0#gid=0|link>

These customers were justifiably frustrated and most were scared that their account got deleted. The team acted quickly and went from design to launch in 3 weeks! Releasing the fix on 06/12!

:jumpingstar: *What did we launch*
We launched a feature in Account Setup that allowed customers to sign in with a different Account in Account Setup. This was inspired by the customer interview for one of the customers that was frustrated with the experience #D4D.

Figma of the experience: <https://www.figma.com/design/GBQDv39wdSPk1IIomjTu46/GSSO-Escape-Hatch?node-id=2-5046&t=XosZdFdz5YdyWoyA-0|link>

 :shark_yay: *Analytics Insights:*
• Splunk dashboard: <https://mailchimp.splunk.intuit.com/en-US/app/search/obx_as_escape_hatch?form.dd_Zhhb8Y5R=%2A&form.global_time.earliest=-24h%40h&form.global_time.latest=now|link>
 
:celebrate: *Why this is big:*
• Potential churn impact for existing customers frustrated with the experience. 
 
:hug:*What is next:*
• Continually monitor VOCs and analytics
    ◦ Note: Since this was released, we have seen almost no VOCs released to this issue anymore. BIG SHOUTOUT to the team for this effort and velocity. 
 
*Special Shout Out:*
:clapping-1772: _*This velocity and amazing turn around of the project would not be possible without this amazing team:*_ 
• Product: <@U03AME5740K|Chima Okechukwu> <@U06QRS4SEBC|Rianna Schanno> 
• Design: <@U02104JK78A|Haemin Hwang> <@U03K5MLFBS4|Chris Sywassink> 
• Eng: <@U03C6DP87PF|Mostafa Derakhshan> <@U07RGQRETAL|Snehalaxmi Avala> <@U03777BQK0B|Elaine Xue> <@U060RFM8D27|Kranthi> 
• TPM: <@U02KZTXSPTK|Erica Jones> 
*THANK YOU*
• _For pushing a customer-obsessed mindset_
• _For being flexible and prioritizing a fix for a churn driver for existing customers_ 
• _For executing with such rigor and velocity_

Thread: 1 replies (latest: 2025-08-04 08:02:29 PDT)
Reactions: rocket_launching (9), sonic (4), clapping-all (3)

---

=== Message from Chima Okechukwu (U03AME5740K) at 2025-08-01 13:49:08 PDT === 
Message TS: 1754081348.476529
_*#SHIP IT:*_ :green-light-siren::green-light-siren:
:rocket-launch::rocket-launch:  *Launched LEGO (App Fabric) for the Default Entrypoint* :rocket-launch: :rocket-launch: 

:emailintensifies:*Executive Summary*
The team is excited to announce that we have successfully migrated our Account Setup flow to App Fabric for the default entry point, with the GSSO entry point coming soon :eyes:. With both changes, we'd now have roughly >95% of our incoming traffic on App Fabric. This unlocks several out-of-the-box features that will drastically improve speed to market for our customers. It also setups us up a strong foundation for us for Fusion!

With this launch, the team gained valuable insights and learnings, which they use to support other teams like SMS and Homepage as they onboard to App Fabric (executing our #strongerTogether). This work has now expanded to include "platformizing" onboarding, to reduce duplicative work for other teams.

:jumpingstar: *What did we launch*
We successfully migrated our Account Setup flow to LEGO (App Fabric).

Figma of the experience: <https://www.figma.com/design/TpxdvVph2XowIkdjznPdG2/Onboarding-Experience---Mailchimp?t=rsSCyRrEm5743vtS-0|link>

 :shark_yay: *Analytics Insights:*
• Quick dashboard: <https://app.amplitude.com/analytics/intuit-portfolio/chart/7grpbjxl?bulk=true&s.name=User+Properties&linkingDashboardId=u80kvt1h|link>
• Tableau Dashboard: <https://tableau.a.intuit.com/#/site/MChimp/views/GTKMDashboardECS/GTKMSummary?:iid=1&:redirect=auth|link>
 
:celebrate: *Why this is big:*
• We're "platformizing" onboarding and making it easy for experiences accross the ecosystem to migrate to AppFabric
• Concrete versioning, rollbacks/releases in seconds, deployments in minutes! 
• Foundational work for Fusion. On App Fabric, we get a seamless transition to Fusion. 
 
:hug:*What is next:*
• Monitor the experience
• Continue working on "platformizing" and migrating other entrypoints to AppFabric
*Special Shout Out:*
:clapping-1772: _*This work would not be possible without this amazing team:*_ 
• Product: <@U03AME5740K|Chima Okechukwu> <@U06QRS4SEBC|Rianna Schanno> 
• Design: <@U02104JK78A|Haemin Hwang> <@U03K5MLFBS4|Chris Sywassink> 
• Eng: <@WRHEEP39A|Mehrshad Sahebsara> <@U03C6DP87PF|Mostafa Derakhshan> <@U060RFM8D27|Kranthi> and the awesome <!subteam^S063NQFRQSU> team
• TPM: <@U02KZTXSPTK|Erica Jones> 
• Thanks to our leaders for empowering the team: <@U08KK7S6LAZ|Diana Williams> and <@U06K8UTTSJE|Jing Wang> 
*THANK YOU*
• _For leading and pioneering the App Fabric migration_ 
• _For executing our #StrongerTogether values as you support and onboard other teams to App Fabric_
Thread: 1 replies (latest: 2025-08-04 09:47:40 PDT)
Reactions: rocket (13), heart (3)



---

=== Message from Chima Okechukwu (U03AME5740K) at 2025-08-01 14:19:05 PDT === 
Message TS: 1754083145.456679
_*#SHIP IT:*_ :green-light-siren::green-light-siren:
:rocket-launch::rocket-launch:  *Launched Model driven Integration Full Screen takeover for Non-Ecomm*:rocket-launch: :rocket-launch: 

:emailintensifies:*Executive Summary*
Today, we interdict self-reported E-comm customers to connect their store after Account Setup. This was run as an experiment in June 2024, and saw a 40+% increase in EComm Integration connections (<https://docs.google.com/spreadsheets/d/1oMjIiUaNH9ra2j7dFcr0fj0N3dK2bRYoUuUZ6HlhiPw/edit?gid=89328829#gid=89328829|Details>). Customers who integrate reach a higher payoff and have a higher retention with MC (<https://docs.google.com/presentation/d/1hvp5XpKdm5C0S2-fN6dILdqsQY7nZrsqJfdA2kusr68/edit#slide=id.g2d8f821de17_0_339|source>), therefore we see huge opportunity to increase our connection rate for non-Ecomm customers by surfacing integrations that we identified from web-scraping and 3-party sources.

At the conclusion of the experiment, the team saw a *6pt lift* (50% increase) in 7D Connection Rate for Non-ecomm customers! :woahman: This lift was even maintained on 14D and 21D Connection Rate!

:jumpingstar: *What did we launch*
We launched a Full Screen takeover for self-reported Non-ecomm customers showing a recommended list of integrations based on our AI model and their web-scrape data.

Figma of the experience: <https://www.figma.com/design/2Vn1pdU7SllB3aeuj6Tgen/Expanding-Integrations?node-id=0-1&p=f&t=RqebDWuG7ZI9f85J-0|link>

 :shark_yay: *Analytics Insights:*
• Analytics readout: <https://docs.google.com/presentation/d/1yf20Vx6VOlnmtSoBHumGDPa51CLO1ROVwxlzxjUzrVE/edit?slide=id.g2791d02e400_1_31#slide=id.g2791d02e400_1_31|link>
 
:celebrate: *Why this is big:*
• Big opportunity to reduce churn by promoting connections to our strategic integrations. 
 
:hug:*What is next:*
• Upcoming experiments:
    ◦ Experiment with an enhanced model that prioritizes more valuable integrations and supports geo-specific integrations.
    ◦ Expand recommendations to the Setup Card to support one-shot recommendations.
• Leverage the Integrations Recommender AI model in other areas of the app to drive more customers to connect their apps to MC
*Special Shout Out:*
:clapping-1772: _*This work would not be possible without this amazing team:*_ 
• Product: <@U03AME5740K|Chima Okechukwu> <@U06QRS4SEBC|Rianna Schanno> 
• Design: <@U02104JK78A|Haemin Hwang> <@U03K5MLFBS4|Chris Sywassink> 
• Eng: <@U06PSKLD0F5|Anastasia Arnold> <@U063JM5UW5P|Alex Vovk> <@U060RFM8D27|Kranthi> and the awesome <!subteam^S063NQFRQSU> team
• TPM: <@U02KZTXSPTK|Erica Jones> 
• Special thanks to the AI Data Science and ML team: <@U02VDMANQPL|Matt Bernstein> <@U02KJF48Q85|Robert Pienta> <@U02KJH3RQTX|Utku Demiroz> <@U02KJC6C1EH|Jing Wang> <@U07BBBC4V2Q|Vishesh Dosaj> and <@U05UFDQC4F6|Mark Spurgeon> 
• Thanks to our leaders for empowering the team: <@U08KK7S6LAZ|Diana Williams> and <@U06K8UTTSJE|Jing Wang> 
*THANK YOU*
• _For amazing work driving more customers to integrate_
• _For an awesome collaboration_

Thread: 4 replies (latest: 2025-08-05 06:12:03 PDT)
Reactions: fire (15), ship (8), rocket_launching (11), heart (4), raised_hands (1), raised_hands::skin-tone-4 (1)
Files: OBX Integration Recommendation NonEcomm - WIP (ID: F096A4V1D5H, application/vnd.google-apps.presentation, 0 Bytes)



---

=== Message from Payton Camilli (W012EU6L7FG) at 2025-08-06 09:31:56 PDT === 
Message TS: 1754497916.405579
:rocket: *Launched: Omni-channel API Public BETA Release (ELC API)!* Full release summary <https://wiki.intuit.com/display/ACS/25.07.28+-+Sprint+26%3A+ELC+API+Public+BETA|here>.

:sparkles: *Customer Problem:*
I AM a developer working for high value Mailchimp SMS customer
TRYING TO set up a custom integration using an API key to bring contacts into Mailchimp automatically
BUT I cannot bring over the full contact list
BECAUSE only contacts with emails can be brought over using the /audiences/{audience_id}/contacts… endpoints
WHICH MAKES ME FEEL like Mailchimp is not equipped to handle my employers use case

:question2: *What changed?*
    ◦ Until now, our public API relied on the presence of an email to allow users to manage their contacts. SMS only contacts were not fully supported.
    ◦ We've launched new /audiences/{audience_id}/contacts… endpoints as alternatives to /lists/{list_id}/members… endpoints. These new endpoints allow for the management of contacts with just email addresses, just SMS phone numbers, or both channels. These API endpoints are still in BETA but include the following capabilities: create, update, read, forget, and archive contacts.
    ◦ The new "omni-channel" API endpoints are being built alongside the existing endpoints, so there will be no breaking changes for current users and C1's who would benefit from this new endpoint can migrate at any time.
:clap-clap: *Why is this a big deal?*
    ◦ Mailchimp SMS users who would benefit from custom integrations can now sync their full contact list
    ◦ Externally managed integrations can update their code to support ingestion of SMS only contacts
:books: *Resources*
    ◦ <https://wiki.intuit.com/display/ACS/25.07.28+-+Sprint+26%3A+ELC+API+Public+BETA|Release plan>
    ◦ <https://mailchimp.com/developer/release-notes/new-audiences-endpoints-beta/|Release note>
    ◦ <https://mailchimp.com/developer/marketing/docs/audiences-introduction/|Developer page (new concepts & disclaimers)>
    ◦ <https://mailchimp.com/developer/marketing/api/audiences/|API reference (new endpoint details)>
:chart_with_upwards_trend: *How's it performing?* Will share wins & learnings in this thread as we go! (<https://mailchimp.splunk.intuit.com/en-GB/app/search/audience_management_-_executive_summary_dashboard?form.contact_events=%22ContactCreateRequest*%22&form.contact_events=%22ContactUpdateRequest*%22&form.global_time.earliest=-24h%40h&form.global_time.latest=now&form.is_hvc=*&form.show_excluded=context.user_id+%21%3D+176433649+AND+context.user_id+%21%3D+177963593+AND+context.user_id+%21%3D+217350298+AND+context.user_id+%21%3D+218799646+AND+context.user_id+%21%3D+219651206+AND+context.user_id+%21%3D+223147458+AND+context.user_id+%21%3D+223510350&form.show_internal=context.user_is_internal%3Dfalse&form.service_name_filter=context.service%3D*&form.caller_filter=*|splunk>)

:next: *Whats next?* Upsert capabilities, react to early user feedback, enable top integrations to ingest SMS only contacts

:mega: *Who made this possible?* :mega:
    ◦ *Audience team:* <@U087Q34S3T6|AJ Hundal> <@WP0ENL12Q|Deepak Mirani> <@U02K6JTS4H5|Eddie Ornelas> <@U03FZ581XTR|George Nakkas> <@U03U7NB1P24|Jake Catron> <@U04H19CEB9S|Jack Naughton> <@U091MQW7VUP|Kyle Jones> <@U04FF36UREJ|Lina Lozano Oviedo> <@U03PXS338NA|Mike Mannix> <@W019Y5V05UG|Mohammad Habbab> <@U03DJNFKW4T|Nicole Robinson> <@U05LRND7CPN|Nikhil Monga> <@W012EU6L7FG|Payton Camilli> <@U02KMFE1ELT|Rolf Martin-Hoster> <@U07USKD0MA5|Shefali Dalal> <@U02K6RNC43Z|Takuya Yoshikane> <@U03Q93CUAHY|Terry Keeney> <@W8FMAA7S8|Yi Zhang>
    ◦ *GTM partners:* <@U06V0MUJNC9|Brooke Frazzetto> <@U07M9BERF36|Christina Park> <@U04G8EQ3S83|Erin Tapp> <@U02KMCPM403|Katie (Bebop) Brennan> <@U02RGGQ757U|Laura Adams> <@U02KJDA2QSH|Maegan King> <@U06M322289M|Miles Kim> <@U02KEMFCE86|Missy Hayes> <@U04AMG9F9QX|Nash Kamal> <@U02PHER72E6|Rai Robledo, MFA> <@U03HRFYTYUB|Simone Kovacs> <@U02KEQJS3LN|Wade Burrell>
    ◦ *Partnerships team:* <@U06JD94AGE9|Ben Ramsey> <@U02LB2S0TNC|Keith Baxter> <@U02LB4VC4UQ|Nate Ranson (he/him)> <@U02KJFNSB6H|Philip Allen>
    ◦ *Leadership:* <@U073E89S8RG|Alek Liskov> <@W8FHXCZSP|Saikat Mukherjee>

Thread: 23 replies (latest: 2025-09-18 07:39:27 PDT)
Reactions: cowboy-frog (15), nice-osrs (18), clapclap (26), blob_cat_sms_intensifies (12), yay (12), frogehappy2 (11), alert (9), this (5), party-blob (7), rocket (6)



---

=== Message from Curt Shearer (U02KZSQSXAM) at 2025-08-07 12:24:50 PDT === 
Message TS: 1754594690.173609
:moneyfred: Enhancing the Sales team’s close process for new paid customers :celebrate:

The Monetization team has developed a new _Sales Offers_ tool within MCAdmin to expedite the conversion of prospects to paid customers. This tool enables sellers to configure unique signup links that include the ability to pay for a negotiated deal.

This innovation eliminates a previously cumbersome and inefficient process which required new customers desiring a high-value, discounted paid plan to first create a free account in order to then gain access to their discounted plan once the account was created. Now the new customer can signup and pay their discounted price in one session. This will also benefit non-discounted plans by enabling sellers to get customers setup on their behalf right away!

Training will be held for Sales managers and sellers in the coming weeks.

Our goal is to get 90% of the offers created with the Sales Offers tool converted to “purchased.” Since this tool eliminates a number of steps from the close process, we expect Sales experts *closing deals 10 days faster* than they currently do and *reducing the number of deals lost by 7.5%*. The additional won deals should *increase the quarterly average new MRR by $40K* (an aggregated total from all Mailchimp Sales teams).
Thread: 10 replies (latest: 2025-11-17 12:49:13 PST)
Reactions: clapclap (41), partying_face (27), yes3 (12), awesome (9), the_horns (2), raised_hands (3), the_horns::skin-tone-4 (1), raised_hands::skin-tone-4 (1), raised_hands::skin-tone-5 (1), the_horns::skin-tone-5 (1)



---

=== Message from Elizabeth Bertasi (U06QWR7FV9T) at 2025-08-12 12:15:31 PDT === 
Message TS: 1755026131.238449
:rocket: :cjb: :new: *ALL existing automation triggers have been migrated to our new event-driven processing system*!

:search-pin: *What’s new?*
We are moving from a monolithic, poll-based system into a modern, event-driven architecture. This transformation will enable near real-time processing, enhance scalability and reliability, and reduce operational costs. All automations are now triggering via monolith-generated event processing, which is our first public-facing step toward achieving our vision.

:analytics-graph: *Impact & metrics:*
_Automation trigger processing has reduced from a median of 76 seconds to 3 seconds*!*_ :ultra_fast_parrot: :speedracer:  This is a HUGE improvement and provides a tangible benefit to our users who want to ensure their automations are reaching their customers in a timely manner.

:coming-soon-icon: *What's next?*
We'll work on activating new data in this system - all new triggers will use this architecture!

:clap: :clap: *Shout outs:*
Thanks to the brilliant and talented CJB team that made this happen!
<@U02KJ1UDHC5|Bobby Craig> <@U02KZQKLPR7|Chris Pitts> <@U03GVFDGUKA|Cliff Martin> <@U03GE2Y59M0|Dana Winn (Automations Oncall)> <@U03UER0JRMY|Scott Stewart> <@U02KZU660AV|Jameson Brown> <@U02KMC0QGSW|Justin E. Samuels> <@U02KMDU1TU2|Maxwell Reich> <@U02KMGM5D98|Yena Ku (they-them)> <@U03UER0JRMY|Scott Stewart> <@U08QM8N05EX|Ranvirsinh Raol> <@U02KMBNL2UB|Jena Powell> <@U02P9STSQGZ|Becca Walsh> <@U02KZMX4E6M|Celeste Mora (they/them)> <@U02KMBDS7AP|Heather Dartz> <@U06QRS4SEBC|Rianna Schanno> <@W8F4X8325|Thomas McMillan> <@U07AX5J7MFB|Eric Anderson>
Resources:
<https://docs.google.com/document/d/1zeYsO1YuiZEMudIDQuBpkR2fqwCMaqUa-HU7pEhZaQY/edit?tab=t.0#heading=h.nbtez4y35hvv|Architecture Vision Doc> | <https://docs.google.com/document/d/1yewjbCbrrnmw-FeOTMYvrLUcSUNdyIqmv1sG22W0v6k/edit?tab=t.0#heading=h.l80faydfywt1|Tech Spec>
Thread: 3 replies (latest: 2025-08-12 13:12:23 PDT)
Reactions: letsgoooo (15), sonic-2045 (15), clapping-all (13), wow-frog (7), shipitparrot (3), raised_hands (1), tada (2)



---

=== Message from Rachana Pejaver (W8FQC6BHT) at 2025-08-13 13:23:23 PDT === 
Message TS: 1755116603.296019
:rocket: *Wrapping up FY25 with 3X growth in 3 Star Data Maturity*  :rocket:
Wrapping up FY25, we have made a huge leap towards ensuring Intuit’s data is trustworthy and reliable with *78% 3 star compliance* - this is a *37 point* (41% - 78%) increase since Q3 and *51 point* (27% - 78%) increase since the beginning of FY25.
Here are a few key milestones to highlight our progress:
• Data Maturity continues to be an *ongoing metric in TOS* via the <https://qliksenseprd.a.intuit.net/sense/app/05966abb-5e6d-4800-b21d-6818da03a890/sheet/88c16e90-7610-47be-9e6c-b73101b3c2c9/state/analysis|data maturity dashboard> - elevating the importance of data maturity across Intuit. This kind of exposure is already driving better data management practices, stronger collaboration, and alignment company-wide.
• Data maturity is now in *regular op-mechs of 12 VP/SVP’s* across Intuit with each team diligently charting out strategies to elevate all their assets.
• *Ten L0 capabilities are now more than 95% 3 star compliant* - Income Tax, ProTax, Monetization, Security Technical Compliance Risk & Fraud, Embedded FinTech, Enterprise Architecture, Enterprise Ecosystem, Customer Growth and Engagement, Identity.
• All teams across Intuit’s ecosystem have accelerated 3* data, with the following *3 L0 teams making the biggest improvements* in the last month
    ◦ CRM & Marketing/Mailchimp (Jack Tam)- up 62 points (16% - 78%)
    ◦ Development Ecosystem (Chris Kasten) - up 49 points (12% - 61%)
    ◦ Data (Sembian Krishnamurthy) - up 40 points (28% - 68%)
• *200+ queries resolved* via dedicated channel (<#C06GZFXFX27|data-maturity-score-support>) and office hours and 150 Jira tickets processed.
• More than *90 data producers* recognized in Q4 with Intuit Badges for their contributions to data maturity
• *562 data workers* across the company have successfully completed the <https://degreed.com/pathway/m90g10qg86/pathway|Data Stewardship Onboarding Degreed training> this fiscal year - further underscoring the company-wide commitment of data producers to ensuring clean, trustworthy data
These milestones are a testament to the hard work and dedication of everyone involved. Let's keep up the momentum and continue to push the boundaries of what we can achieve with data at Intuit.

:next: *WHAT'S NEXT*
We will continue to drive operational rigor around data maturity in FY26 with a focus on 4 star data.  Data Capability teams are also hard at work to provide updated 4 star data standards and paved path capabilities to enable the promotion of data to 4 star. More information on this will be shared in the coming weeks.

:thankyou1: *THANK YOU*
• *Data Maturity Dashboard* - <@WJW7BFN0H|Matthew Gigliotti>, <@WJR44QWMQ|Karen Maciolek> <@W8FQC6BHT|Rachana Pejaver>
• *Data and AI* *Capability PD, PM, Analysts and TPM* - <@U07RYMAF59R|Kedar Narwadkar>, <@W8FHWPPHR|Chaitra Rao>, <@U02BVMLUQ2J|Ashish Page> <@W8FQATQ2H|Jainik Vora [upcoming OOO - 5/4 to 5/15]> <@WB03ZN0S0|Tapan Upadhyay> <@WNZT8RWG1|Prema devi Kuppuswamy> <@W8FL3E98A|Smita U>  <@U027FRUQH97|Megha MT> <@W8FQD6NPP|Byron Stecklein> <@U02V54ZGYUS|Katyayani Rajput> <@U05MPFKPWPQ|nandor (858-442-1888)> <@U08KS843Z3M|Navneet Goel> <@WK4FENYUF|Sam Knapp> <@U01MH87RRLM|Paul Stanford> <@U01E051DWKZ|Juhi Dhingra> <@U040WPJSE9K|Kratika Bandi> <@W8TUUB4DT|NS> <@U042VR1K7B8|Monica Singh> <@U01URECPUBZ|Isaac Obamehinti>
• *Cross Intuit TPM drivers, TPM leaders and POC-* <@WDFBHVDLY|Alyssa Cherry>, <@W8N2ZEUMC|BJ Wahl> <@W8FL2KM3L|Athmika Vishvesh> <@U04SSK4GA5T|Hyder Heisman> , <@W8FQB11QV|Katie Besgen> <@U03B51N6A4Q|Amukta> <@U02NE72N3CP|Razila Farzeen> <@W8FQBVCBF|Kyle Rose> <@W8R92RSJ2|Aleksandar Yordanov> <@U03B51N6A4Q|Amukta> <@W8FL2KM3L|Athmika Vishvesh> <@WQAJJGLMU|Ben Alarcon> <@U079GDD2EUR|Ben Irwin> <@W8FL3EK7U|Chetan Janbandhu> <@U02L0R54J81|Dhruv Kaushik> <@W8FHZSVT5|Gaurav Khanna> <@W8FM9ALDA|Guergana Yordanova> <@W8FL3VB34|Harish Gundecha> <@W8GN4C6CX|Harish Viswanathan> <@U06PFFCTRQR|Neeru Jain> <@U02KJASFMS9|Homer Bartlett> <@U04SSK4GA5T|Hyder Heisman> <@W8GG8NF8E|Jennifer del Rosario Bollish> <@W8FQB11QV|Katie Besgen> <@W8FM9NH60|Kedar Bhatt> <@U02K6NWDM7H|Marlene Mayfield> <@W8GN540KZ|Ravi Pillala> <@U06TXS3V8R1|Ritu Sabharwal> <@W8GJWLTC6|Sam Kaul> <@W8FL48RKL|Shankar Chittoor> <@W8GG6RYR4|Snehal Shirole> <@U08M7HJ49U7|Sudeep Kaushik> <@U048M31892N|Tony Gauda> <@W8GG5UJ30|Tyler Vallillee> <@W8F0REA6L|Vivek Arya>
• *Leaders -*  <@WJR44QWMQ|Karen Maciolek>, <@WJW3CV4E5|Allison Bellah> <@WK4FENYUF|Sam Knapp> <@W8FMAM7EY|Achal Kumar (858-200-6816)> <@W8F0RSJJC|Arun Ragothaman> <@W8FQCED37|Sembian Krishnamurthy> <@W8GN4A3PZ|Tristan Baker> <@W8FQEKSHK|Ashok Srivastava> <@W8FL4UK0A|Krithika Swaminathan (650-336-4016)>

Reactions: rocket (6), tada (1), awesome (1)



---

=== Message from Frank Persico (U03KUBTCSG1) at 2025-08-26 12:10:57 PDT === 
Message TS: 1756235457.026699
*#SHIP IT: What We Launched* :rocket:
Hi all! Excited to share that the segmentation team recently launched a new set of enhancements that allow users to target their campaigns based on customers' browsing activity in Shopify. This feature gap was a regular source of requests from our ecommerce ICP customers as well as a visible area where we lagged behind competitor offerings so this launch marks a significant step forward in elevating our product experience. Thanks to the close partnership between the Audience & Segmentation, Integrations, and CDP teams this release will add material value for our DSB customers, both on its own and as part of the suite of ecommerce enhancements going out across Mailchimp.

*The Customer Problem* :slightly_frowning_face:
Our roughly 45,000+ Shopify-connected customers lacked the ability to target their bulk campaigns to contacts based on where those contacts were in the purchase funnel because segmentation was limited to customers that had placed orders. Users could send re-targeting campaigns to these contacts, but if a contact added a product to a cart recently the only way to market to them was via an automation. This experience gap was particularly pronounced in comparison to Klaviyo, who already offer a robust set of ecommerce segmentation options that include these browse actions.

*The Solution* :blob_thumbs_up:
As of today all users in Standard and above plans that have a Shopify store connected to their Mailchimp account have been given access to several new ecommerce segmentation conditions. Some examples of the segments users can now create include:
• Contacts that started checkout but haven’t finished making a purchase
• Subscribers who browsed the page for a specific seasonal product within the last month
• Contacts that added a product to their cart with a price over $100
This unblocks customers from being able to send bulk messages to their contacts that are considering making a purchase but need additional marketing to move them to the next step in the funnel.

*What's Next* :next:
Next we'll be adding more ecommerce segmentation options for product collections, new data aggregation options, and more order statuses in order to give DSB customers even more options for how to tailor their marketing and convert their contacts. Outside of ecommerce, these same segmentation conditions will also be utilized to support the Blotout integration, which is also planned to roll out in the near future.

:champagne: *Please join me in thanking the people that brought these improvements to life!*:champagne:
*<@U05KZB08WRY|Jon Griffin>* *<@W8FJ04FH9|Andrei Khmelnitski>* *<@U03H4220CK0|Yoel Gonzalez>* *<@U072QE8MQ05|Jessica Rocha>* *<@U07A31AD7UZ|Thomas Grundy>* *<@U07S0HEP5T9|Jared Malcolm>* *<@U07U1NNUHRC|JP McConnell>* *<@U02KEEED9LN|Amit Khare>* *<@U07Q70L7BC5|Vova (Vladimir) Shechtman>* *<@W019Y5V05UG|Mohammad Habbab>* *<@U02KJENBBDK|Neveen Moghazy>* *<@U073E89S8RG|Alek Liskov>* *<@W8FHXCZSP|Saikat Mukherjee>* *<@U03HRFYTYUB|Simone Kovacs>* *<@U086MMX7W0M|Juliana Simoes>*
Thread: 13 replies (latest: 2025-09-09 11:01:00 PDT)
Reactions: rocket (40), oooooo-1912 (16), yes3 (15), star-struck (8), shopify-intensifies (5), ayyyyy (1), champagne (1), cat_clap (5), clap::skin-tone-2 (1)
Files: S2S Gif.gif (ID: F09C342UBNH, image/gif, 3.7 MB), image.png (ID: F09C6GWG47Q, image/png, 59.5 KB)



---

=== Message from Diana Williams (U08KK7S6LAZ) at 2025-08-26 12:27:23 PDT === 
Message TS: 1756236443.152279
Love it!! 
Reactions: rocket (1)



---

=== Message from Marissa Rivera (U02LB3HSDRN) at 2025-08-27 10:16:46 PDT === 
Message TS: 1756315006.275279
:rocket: *Transactional SMS Beta Release* :rocket:
<https://wiki.intuit.com/x/kNMKVQ|Transactional SMS> is now available in Beta for select Mailchimp customers!

We’re excited to announce the Beta release of Transactional SMS, expanding our transactional communication services beyond email.  With this new offering customers can now send automated, one-to-one text messages triggered by specific actions or events, complementing our existing transactional email product.

Transactional messages, like account alerts, purchase confirmations, and password resets, are essential to customer trust and engagement. Many of these notifications are time-sensitive. SMS provides the speed and direct reach businesses need to ensure their customers never miss a critical update.

*What’s Next* :next:
This Beta marks an important milestone in our long-term strategy to invest in and grow our transactional services. We’ll be gathering feedback to refine the experience, improve performance, and ensure it scales effectively before general availability, which is currently targeted for early Oct. 2025.

:thankyou1: A big *thank-you* to the Transactional team and our cross-functional partners who made this happen!!

*Tx:* <@U02KJAK7GA1|James Moriarty> <@U02L01LC801|Matthew Grove> <@U02KZVD44TT|Jon Shogren> <@U02KPJ01EVA|Josh Campbell> <@U06F2GL3WRY|Ahmadullah Aminy> <@U02L0377N81|Patrick Murphy> <@U02KPG6UT44|Drew Frezell> <@U07UC8T8EQ6|Karen Robertson> <@W8VQ73C8P|Ashwini Sriram>
*SMS:* <@U07NM1TFPAB|Zach> <@U03J3GGU5T3|Jeremey Nofzinger> <@U03NU55364D|Satish Sambandham><@U02LANRD7R6|Adam vanWestrienen> <@W013E2DDP3J|Alina Rainsford> <@U03TDLSFYH0|Ben Marks> <@U06QHNDKYQK|Leo Lin> <@U076PQ83WPJ|Ana Bell> <@U06R90N9A6N|Suzanne Kirkpatrick>
*GTM Partners:* <@U04G5KNNVUM|Katie Witkowski> <@U02L01GJVC1|Mansi Gupta> <@U06P00YMHS7|Steve Lindberg>
*CTREC:* <@U08EWUEJZNC|Sarit Ashtar> <@U08637A29EX|Hao Tan> <@WFBQDKXMW|Ifat Friedlander> <@U02LAV5UQQ0|Blair Sullivan>
*PLC:* <@U02KZSQSXAM|Curt Shearer> <@U05NALW1S3U|Collins Amadi>
*Leadership:* <@U07AX5J7MFB|Eric Anderson> <@U02KJBP43V3|Jess Riddle (She/Her)> <@U02LB66UA1E|Shani Boston> <@U02KJF76MU5|Rujuta Apte>
Thread: 10 replies (latest: 2025-09-18 10:55:17 PDT)
Reactions: blob_cheer (31), clapping-all (22), sms1 (12), yayyy (12), cellphoney (10), blob_cat_sms_intensifies (9), lets_go (8), extreme-teamwork (7), party-wizard (6), mandrill_but_cool (4), orange-flame (1), raised_hands::skin-tone-2 (1), raised_hands::skin-tone-3 (1)



---

=== Message from Laurie McGowan (U02KMCPC99R) at 2025-08-27 10:45:42 PDT === 
Message TS: 1756316742.646909
:sparkles-pink:  Get ready! The official kickoff of our *Mailchimp Innovation Council (MIC)* is coming up the week of *September 8!* See Matt’s post <https://intuit-teams.slack.com/archives/C03TNEENK9A/p1756141664979179|here>.

:light:_What is it?_ 
MIC brings together customers, partners, prospects, and thought leaders whose expertise and insights we’ll tap into to help guide our product roadmap and strategy. Matt will kick off with an overview of Mailchimp’s strategy, then members will immerse themselves in a Gallery Walk, several deep dive sessions on agentic AI, omnichannel and partnership opportunities, the Intuit Platform Vision, and reporting and data needs, as well as meet & greets with other teams and leadership.

:action-points: _How can I participate?_ 
While members will be busy with workshops during the day, we’re inviting anyone across our org to come and mingle with our guests at our mixer on *Wednesday, September 10, from 5 - 7 p.m. at Moonlight* inside The Forth Hotel.

We'll have drinks, snacks, a photobooth, and a DJ to close out our first day! This will be a great opportunity for you to meet the 2025 MIC members as they wrap up their visit. :clinking_glasses:

Space is limited, so please sign up for our MIC Mixer by Wednesday, September 3, to secure your spot. By signing up, you'll be automatically entered into a raffle for a chance to win 1 of 5 Yeti Coolers! Winners will be contacted after the mixer. Check your inbox! :gift:

:snap-point-flip: *<https://form.jotform.com/252327249942159|RSVP> by Wednesday September 3!*

:book:  _Where can I learn more?_
Learn more about our program and each of the members joining us <https://docs.google.com/presentation/d/1Euzk0oG6-qs_1wx9fkg4ryDQwxkGot6gksuX8ABkwOc/edit?slide=id.g37b54260c75_0_0#slide=id.g37b54260c75_0_0|here>.
Reactions: oooooo (6), clapping-all (6), yay3 (3), happy-customer (2)



---

=== Message from Cassandra Marshall (U07B5L5983F) at 2025-08-27 14:38:02 PDT === 
Message TS: 1756330682.848369
:rocket_launching: Actionable Insights Experiment!
This experiment is the first step toward Mailchimp becoming a trusted, proactive marketing advisor. It surfaces *actionable insights* directly on the homepage, helping C1s turn performance data into clear next steps that drive adoption of high-value Mailchimp features.

:light: Opportunity
This initiative delivers a focused set of actionable insights designed to help SMB (C1) customers confidently take the “next best action.” By surfacing guidance on the homepage, we reduce friction, close strategy gaps, and ultimately drive higher engagement, retention, and revenue.

:customerproblem: Customer Problem
I am an SMB customer.
 I can see how my campaigns perform, but I don’t know what to do next.
 Without clear guidance, I default to the same limited playbook, even when it underperforms.
• Customers underuse Mailchimp’s most impactful features (segmentation, automations).
• In a year, the median marketer only sends 8 out of 76 types of campaigns, leaving proven growth levers untouched.
• VOC shows repeated demand for “better, deeper, more actionable insights” that help users separate what they _could_ do from what they _should_ do.
*Customer Quote*
 _"Like I'm just not looking for Mailchimp to report numbers. I also want it to act like a marketing strategist and give me actionable insights and how to optimize. You have so much data in Mailchimp and dont use it to help me."_ — VOC Slack Feedback

:chart_with_upwards_trend_intensifies: Solution
*Phase 1: Homepage Experiment*
• *Insights:* Up to 3 insights displayed in standalone containers.
• *Launched Insights:*
    a. _New Subscribers_ → Create a welcome segment.
    b. _Grow Your List_ → Set up a popup form. (Fast Follow)
    c. _High Intent / No Order_ → Create a segment of recent clickers with no purchases.
    d. _Recent Email Performance_ → View top-clicked campaigns.
• *CTAs:* Each paired with a direct, high-value action and a DFY experience.
• *Plans:* Standard+ customers; Email and SMS channels supported.
:numbers: Hypothesis / Success Metrics
*Hypothesis*
 IF we surface clear, actionable insights on the homepage, each paired with a recommended next step, THEN C1s will be more likely to complete high-value marketing actions, LEADING to higher adoption of Mailchimp’s most impactful features, stronger retention, and more revenue.
*Primary Success Metric*
• *Insight to Action*: Insights to action (segment creation, form launch, campaign send, automation modification, or report view) post insight engagement.
*Secondary & Learning Metrics*
• CTRs on primary/secondary CTAs. Dismiss rate and qualitative dismissal feedback. Completion rate for actions tied to insights.
• Retention, Mailchimp-attributed revenue, and plan upgrade rates.
:clipboard: Learning Plan
• Launched as an *A/B test* with homepage control group.
• Runtime: 2 weeks, ramping to 100% on Aug 26, 2025.
• Results to come!
:fast_forward: What’s Next
• Fast follow insight: improved _Grow Your List_.
• Expansion to Free plan customers.
• Insights on additional surfaces (Audience, Conversion, Email Report).
• Benchmarks & personalization to contextualize “why this matters.”
• Long-term shift from rules-based → model-driven → AI-generated, with Mailchimp acting as a co-pilot that sets up actions on behalf of the customer.
:shoutout1: The Team, The Team, The Team!
*Reporting and Analytics Team*: <@U02LB1Z7EU8|Justian Meyer>, <@U01SGFG4FU5|Tanushree Chaubal>, <@U03SZ30NENB|Jonathan Davis>, <@W0132PN7VQ9|Connie Huang>, <@U02K6PD6HN3|Michael Heard>, <@U07B02LLNAC|Dmitri Medvedev>, <@U0372SDKQDS|Tiffany Huang> <@U06UVNGHHDJ|Tosin Aiyelokun> <@U07ED705DHS|Aastha Sehgal> <@U02KMG1BGBV|Shane King Zackery (they/them)> <@U092280FEMP|Nitika Korla>
 *Leadership*: <@U073E89S8RG|Alek Liskov> <@U02KJENBBDK|Neveen Moghazy> <@W8Z8R7STE|Nir Harel> <@W8FL6URHQ|Deepak Prabhakaran> <@W8FHXCZSP|Saikat Mukherjee>
*Resources*
• [<https://docs.google.com/document/d/1KdEa9ql72WO_G7Wh7pzLuq4K-ivLUsSAQFleqIl2gDg/edit?pli=1&tab=t.cs9utsw8lbij#heading=h.75s39xuv6gz4|PRD>]
• <https://docs.google.com/spreadsheets/d/1cPBCdzZnJjizeXdTCrVtTX9va27Fcz3q2g_CDMrayjk/edit?pli=1&gid=0#gid=0|Library>
• [<https://www.figma.com/design/y9FBtnAU4B6v0IM0IV8iTY/Actionable-Insights?node-id=2369-240&t=LRFCOcyTKHglBgBo-0|Figma>]
• <https://docs.google.com/document/d/1GBGg-Zu6e0zxLhhafdVxbqg17JWV_-C79AjdknpqSSc/edit?pli=1&tab=t.bgkovzhxulv9#heading=h.4c40og9ra3k3|[Experiment Design Doc]>
• <https://wiki.intuit.com/pages/viewpage.action?spaceKey=MCREPORTING&title=25.08.11--+SPRINT+26--+Release%3A+Actionable+Insights|Release Plan>
Thread: 5 replies (latest: 2025-08-28 17:44:40 PDT)
Reactions: raised_hands (12), cat_clap (9), raised_hands::skin-tone-5 (1), raised_hands::skin-tone-4 (2), fireball (10), raised_hands::skin-tone-2 (1)
Files: Actionable Insights Library (ID: F08R5U2C8EN, application/vnd.google-apps.spreadsheet, 0 Bytes), Actionable Insights Experiment Design (ID: F08Q5M7T5HS, application/vnd.google-apps.document, 0 Bytes), Copy of PRD | Actionable Insights (FY25) (ID: F08R16FKD5F, application/vnd.google-apps.document, 0 Bytes)



---

=== Message from JP McConnell (U07U1NNUHRC) at 2025-08-28 04:31:44 PDT === 
Message TS: 1756380704.387859
:rocket: *Launch: Real-time C2 behavior tracking for Shopify*

:dart: *Why it matters*
Real-time C2 behavior data is critical for Digital Sales Businesses (one of our key ICPs for FY26)  their short, impulse-driven cycles mean most purchases happen within 30–60 minutes.

:wrench: *What’s new*
With the new *S2S Integration + IdGraph*, Shopify users now capture all key signals (like product/collection views) across all their C2s. These map to a unique Mailchimp ID, letting us track behavior over time no matter the source.

:bar_chart: *Scale highlights*
 • 2.3B C2 contact IDs; 0.5B Shopify device IDs
 • 76M mapped (15% match rate)
 • 10.6B behavioral events, 24% mapped to known contacts
 • :zap: p99 latency: <1 sec end-to-end

:rocket: *What’s next*
This foundation powers the new segmentation events <https://intuit-teams.slack.com/archives/C03TLJNADSP/p1756235457026699|Frank shared >Tuesday, plus improvements in reporting (Q1), automations, and more.

:raised_hands: Please join me in thanking the people that brought these improvements to life:
<@U02KEEED9LN|Amit Khare> <@U02KM2QGKEW|Ali Heidary> <@U03TDGU2JUB|Josh Day> <@U07GARRQRHR|Amar Manjunath><@U07B96L9T9N|Adam Mitchell> <@U02KM7L9D7U|Colt Carder> <@U02KJE3FRFX|Michael Plattner> <@U07FRV7RNJX|Tao Zhang> <@U07PNSRLYR5|Tommy Miller> <@U079Y3PKJLQ|Vassilis Dourdounis> <@U04QNS5KEE6|Ajeet Seenivasan>
Thread: 8 replies (latest: 2025-09-09 11:00:26 PDT)
Reactions: dancingdino-3573 (5), rocket (9), neon-nice-2 (6)



---

=== Message from Brittney Muhamed (U02KM90H7R9) at 2025-08-28 11:54:23 PDT === 
Message TS: 1756407263.009859
:rocket-launch:*Modular Homepage (AKA the AppFabric Homepage) is LIVE for all FTUs as of 8/15!*

 :code: *What’s new?*
The FTU homepage is now hosted in AppFabric! While FTUs will see no difference in their homepage experience, the new modular homepage improves scalability and maintainability, reduces technical debt, and enables faster feature delivery. It also aligns Mailchimp with Intuit’s modernization strategy and prepares the platform for future enhancements like deeper personalization by ICP and easier integration with other Intuit products.

:target-4417: *Who gets this experience?*
This experience is live for the First Time User homepage. Customers who signed up for Mailchimp <30 days ago will see the Modular Homepage.

:yay-cat: *Early Wins*
We’re already seeing velocity improvements from the team thanks to the separate git repository for Homepage and reduced api latency.

:horizon: *What's next?*
The homepage team is currently working on the <https://docs.google.com/document/d/1EioZ_oeYDus3O84WGpNep5tT_vqr96Ljl0TAi6fB6oc/edit?tab=t.0|enhancement and migration of key performance widgets for the homepage> including the Audience, Recent Campaigns, Revenue (for our DSB ICP) and Marketing Snapshot.

In early October we will release an experiment that will display these widgets on the homepage for customers soon as they are relevant to their business. This will remove the first 30 day / post 30 days split, creating One Mailchimp Homepage. This effort is our next step toward more personalized experiences for our customers!

:clapclap: *Shout outs:*
Thanks to the talented OBX Homepage team that made this happen - particularly our Engineers who drove this effort!
<@U07NWH50KUL|Raghavendra Bokka>, <@U0428EDN518|Nick Boyle>, <@U03DRMGVA1L|Mary McKeon>, <@U05Q70X0FQC|Ashley Oelbaum>, <@WS6FTU6SX|Kumar Vannela>, <@U0448BHJGTU|Yash Sonani>, <@U045VFLCST1|Jenna Emerman>, <@U05UH8ZM6N9|Maddie Jones>, <@W8FQB94DB|Ravi Channapati>, <@U064V8HNWL8|Kate Bishop>, <@U03777BQK0B|Elaine Xue>, <@U02KZTXSPTK|Erica Jones>,<@U03EEL3PU9H|Sid Kumar> <@U02TP8JFQ4Q|Chris Keimig> <@U06K8UTTSJE|Jing Wang> <@U06QRS4SEBC|Rianna Schanno>

*Resources:*
<https://docs.google.com/document/d/1lSykLHZc0_u11a-0-Xk4vUWEs7d67vGXRFm7NYGTZ4E/edit?tab=t.0#heading=h.t4pqt8uzwu97|Tech Spec> | <https://mailchimp.splunk.intuit.com/en-US/app/search/modular_homepage_100?form.global_time.earliest=-24h%40h&form.global_time.latest=now&form.user_type=false|Splunk> | Feature flag: obx.modular_homepage
Thread: 4 replies (latest: 2025-08-28 20:06:50 PDT)
Reactions: oooooo (16), clapclap (17), nice-pink (7)



---

=== Message from Rachel Shelby (U02TPHN09K7) at 2025-09-03 15:18:54 PDT === 
Message TS: 1756937934.330709
:rocket: *MC Strategic Teams Join CXM & Gainsight* :rocket:

*What we launched (8/11):*
• Migrated all ~75 Strategic Experts across *NA, EMEA, and APAC* from MC Salesforce legacy to *Salesforce CXM* in just *18 hours (8/10–8/11)*
• Migrated Strategic teams from *ChurnZero (*old / deprecated Churn reduction tool) *→ Gainsight*, enabling proactive customer health management, centralized account oversight, and stronger proactive engagement motions
• Transitioned from MC 3P tools → *Intuit 3P tools* for consistency and scale
:mountain: Why it matters :mountain:
This launch unifies all Mailchimp Strategic teams on Intuit’s CXM platform and introduces Gainsight as the foundation for proactive outreach and churn prevention.
Gainsight delivers:
• Health scores to anticipate churn risk
• Stronger engagement signals with playbooks for action
• Centralized account management in one tool
• Richer product insights to guide outreach
Together, these capabilities empower teams to engage earlier, act smarter, and strengthen customer retention.
Learn More About Gainsight  :themoreyouknow:
• Gainsight Demo: <https://drive.google.com/file/d/1jaQ9Bmb6pNuqPozVbxEovQO_1LqiLUPp/view?usp=sharing|Exciting New Features and Improvements in Gainsight!>
• Gainsight Overview Slides: <https://docs.google.com/presentation/d/1auzrQ11-sJXCBfMfiZAJeUBjqAiFp8Qfpb4K0pk7hkQ/edit?usp=sharing|GS CSM Slides>
• Strategic Migration Experience Review: <https://docs.google.com/presentation/d/1kEMYzDEzUebshr9SidtX-fP-fiJtwA2ZZc5uGAGJLgU/edit?slide=id.p2#slide=id.p2|Experience Review Deck>
:next: *What’s next* :next:
• Continued hypercare with prioritized *Gainsight enhancements*
• Streamlining *CXM account layouts* and incremental improvements (e.g., editing a case directly from the proxy widget)
• *Updated churn propensity model* in Gainsight to sharpen predictive signals for retention
• *Account Management scorecard* to measure progress against FY26 goals and drive accountability
• Ongoing tracking of configured workflows to measure *expert impact* and validate success metrics
• FY26 - Deprecate Mailchimp Salesforce
:spiral_calendar_pad: *Looking back* :spiral_calendar_pad:
• This launch caps a *9-month journey* that required a complete pivot away from our original target platform (*B2B*) and suite of VEP capabilities. Instead, we rallied to deliver on *Salesforce CXM + Intuit 3Ps* as part of *Intuit’s ITAD strategy* unifying all of Customer Success and Care onto a single platform: CXM.
:thankyou1: :pray: *Huge thanks* :pray: :thankyou1:
*Thanks to the incredible teamwork and focus across functions. This achievement not only unifies Strategic teams, but also closes out the Mailchimp migration journey — a huge win for Intuit!*

*Teams that made it possible*

• *VEP PM & BSA:* <@U02TPHN09K7|Rachel Shelby> <@U041KFP78A0|Max Wolitzky> <@WGZ0HDUKC|Q> <@U03AMP59HV1|Varsha Menon> <@U02KJ5JHLS1|Carl Chomko> <@U03N01UGXPE|Kym Pressley> <@U03TYGJA7D2|Nick Smith> <@WGZ0HDUKC|Q> <@U02KPKHHZHS|Lily Killingsworth> <@U02KJ5CEADB|Alina Deininger> <@U02KZUTQZQR|Heather Bryant> <@U03MJ3NUAR4|Donna Seapoe> <@U02K6L1664X|Jennifer Maley>
• *VEPCS PD:* <@W8F0RJD0Q|Bharath Brahmakal> <@U03SW565D18|Kunal Dixit> <@U061GGLCERG|Abhiraj Datta> <@W8FQC51FX|Shruthi S>
• *MC Data Eng:* <@U05A4D12BT8|Alexandra Pappas> <@U05B8V54DC0|Rich Archer> <@U02KMFJQ7KL|Sabrina Carbo> <@U07VCUHPXDZ|Dan Piening> <@U02KEKMTNNA|Jenn Reed>
• *MC Data Science:* <@U02K6KBFR7Z|Elizabeth Stanford> <@U08LBSCT9NY|Carlo Bailey> <@U04J0JBPWP2|Sanjay Motwani> <@U05E269C7FH|Dev Parikh>
• *VEP XD:* <@WCN7PNM47|Joe Gardner>
• *VEP TPM:* <@U065C40A99P|Neeraj Soni> <@U03R6AS170Q|Sheraine Leung>
• *Foundations Data Pod:* <@U02DCA5JMFA|Shubhashish Tiwari> <@U06U7586V9R|Shubham Sharma> <@U05R8CMUH7V|Shishir Shivhare> <@U03EQB1M2DC|Binoy Parikh>
• *Foundations:* <@WB294U4UQ|Sean Foley>
• *Sales Enablement:* <@U06L11GPRDH|Kasey Wilson> <@U04HA5T61A6|Zoey Brown>
• *RevOps:* <@U08F67Z8YBZ|Sandeep Kumar> <@U02KM81JD50|Andrew Barrocas>
• *MC Product:* <@U02K6N931JB|Mac Dillard> <@U073ULQ68TG|Tushar Kalbhor> <@U03AME5740K|Chima Okechukwu> <@U06PSKLD0F5|Anastasia Arnold>
• *MC PD: <@U02KMAX8QUT|Jason Veatch>* *<@U063JM5UW5P|Alex Vovk>* *<@WRHEEP39A|Mehrshad Sahebsara>*
• *Mod Ops & CS:* <@W8FHYR9U3|Gregory Williams> <@W8FHYLW3D|Amy Vandemark>
• *MC Quality Center of Excellence: <@U02KPG6G9PW|Gregory Lehman>*
• *Managers - Onboarding & Account Management:*  <@U02LB089DHN|Danielle Lucas> <@U08FL1BSLNM|Cassie Henning> <@U02PWSQQ8A0|Emily McAnnally> <@U02K6NH8RE3|Maggie Heck>
• *UAT Testers:* <@U02692S6XPC|Taylor Boyle> <@U02KJ3TCDPX|Bonnie Watkins> <@U039NUU82EL|Rachel Benner> <@U02P2B0DS67|Sydney Whitehead> <@U0880AS5YBC|Keenen Walker> <@U086R4YLQHE|Brian Elder> <@U06FPTKR067|Rachel Newell> <@U07CFJNQYP3|Kate Stapley> <@U042B8EL61W|Saša Hasanbegović> <@U02K6GL45U7|Anna-Marie Yeskey> <@U060NKPDHF1|Swati Bala Subramanian> <@U07GMUMCCRW|Brittany Williams>
• *LCM & Mar Ops:* <@U04KFJTA613|Tobi Olofintuyi> <@U04BX4EULMC|Drea Latouche> <@U05AL2VAAA2|Mahu Sims>
• *Leadership:* <@U06M58S7AMV|Bobbykin Makwana> <@WS6D85NHE|DeMarcus Simmons> <@U07Q6JN5N6Q|Steve Sanchez> <@U054QGJRYJF|Adam Anger> <@WH3P9023S|Lance Williams - 408-477-0444> <@U01JKQ9BB9C|Shilpa Reddy (she/her)> <@W8FL2QMQS|Anant Saxena> <@W8FHYGK19|Jack Tam>

Thread: 6 replies (latest: 2026-04-14 08:35:57 PDT)
Reactions: woo-hoo (27), clapclap (28), cartwheel-freddie (11), rocket (16), clap-clap (10), celebrate-inclusive (10), tada (11), +1::skin-tone-3 (3), +1 (4)



---

=== Message from Caroline Josey (U033CC0AUD8) at 2025-09-05 13:05:15 PDT === 
Message TS: 1757102715.298179
:rocket-party: *Web Marketing launched Mailchimp Assistant!* A first-of-its-kind Intuit AI chat bot, on <http://Mailchimp.com|Mailchimp.com> for prospective (pre-auth) and existing users.

:experiment: Launched as 50/50 experiment in the US only, our objective is to:
• *Improve user experience* by providing accurate and contextual responses
• *Increase paid bookings*
• *Reduce bounce rates* and time to conversion through engaging interactions
• *Optimize the user journey* by offering actionable next steps and wayfinding

:moneybag:We expect to see an increase in self-serve activations & bookings and sales leads as part of Scaled Acquisition.


:link: <https://docs.google.com/document/d/1AxSGcO7HjNCMzMsjJQvcFYwNNngRFNSMxLUS4V9JvOA/edit?tab=t.0#heading=h.mt8ychc3h5kt|PRD> | <https://mailchimp.splunk.intuit.com/en-US/app/search/mailchimp_assistant_-_dotcom?form.timePicker1.earliest=-24h%40h&form.timePicker1.latest=now|Splunk>


:ty_: Shout outs to <@U02KEKNFZD4|Jon Wallace (jWall)> <@W8F4XD9U1|Arun Avanathan> <@U02KPL46GDS|Munia Rahman> <@U02URC9KK46|Lawrence Ma> <@U02B9R7MAH3|Brian Nguyen> <@U03AQ35Q2P6|Franco Reyes> <@U02KM9USVDY|Greg Clark> <@U02KJ6V3LA1|Cody Solomon> <@U03SHEV00CU|Nylah Julmice> <@U034ZNPP6RH|Leta Negandhi> <@U03ETSQ5A1K|Jeremy Tillman> <@U07KDPW3E3A|Christine Zhu> (and team) <@U064FLW0QAK|Taylor Horton> <@WTDSPU7P1|Anamitra Majumdar> <@U02KENZHH6J|Robyn Taylor> <@U06K8UTTSJE|Jing Wang> <@W8FL5H6E6|Vinay Chandra> (and team) <@U039RUNMK25|Tan Le-Dang> <@U02KEED6LTG|Ankur Bag> <@U02KJEEHTFX|Neil Banchero-Smith> for their work on this project over the past year
Thread: 8 replies (latest: 2025-09-08 08:11:55 PDT)
Reactions: celebrate (21), rocket-party (20), party-blob (11), clapclap (7), dancedoggo (6), neil-vibing-nb (6), catjam-7969 (3), rocket (3)



---

=== Message from Ade Ajanaku (U04925BQ27M) at 2025-09-09 10:01:51 PDT === 
Message TS: 1757437311.778949
:rocket: *Launched: Wix Bookings & Services Consumption* :rocket:

:triangular_flag_on_post: *Customer Problem:*
The previous version of the Mailchimp Wix integration was designed to support Wix Stores and e-commerce C1s by enabling Product, Orders and Contacts data syncing. However, only ~30% of Wix customers are “pure” e-commerce businesses the remaining ~%70 are hybrid professional service based businesses. Furthermore, in the first half of 2025 Wix's professional services verticals (<https://support.wix.com/en/article/wix-bookings-about-wix-bookings|Bookings>, <https://support.wix.com/en/article/about-wix-events|Events> & <https://support.wix.com/en/article/wix-invoices-about-wix-invoices|Invoices>) accounted for ~42% of Wix’s total email marketing volume at ~1.4B emails sent across these verticals from <https://www.wix.com/features/email-marketing|Wix’s native e-mail marketing platform>.

:bust_in_silhouette: *Bookings Customer Problem Statement:*
*I AM* a Yoga Studio owner who actively leverages Wix bookings to manage my Yoga classes, courses and client appointments. 
*I AM TRYING* to view and access my services and active client bookings. But I am unable to do so because this data is not available in Mailchimp. *WHICH MAKES ME FEEL* frustrated and disincentivized to continue to leverage the Mailchimp & Wix integration.

:bulb: *Solution:*
The Mailchimp Integrations team in partnership with IDX, launched a new version of the <https://mailchimp.com/integrations/wix/|Wix integration> to support Professional Services customers that now facilitates syncing a C1’s Services catalog and real-time Bookings Data. This functionality leverages the Lightweight Integration Architecture framework which publishes <https://datamap.app.intuit.com/studio/entity?id=urn:intuit:integrationandautomation:mailchimp:Booking&view=schema|Bookings> and <https://datamap.app.intuit.com/studio/entity?id=urn%3Aintuit%3Aintegrationandautomation%3Amailchimp%3AService&view=schema|Services> to CDP via the MC Event Bus. Eliminating the need to publish this data to the monolith.

:chart_with_upwards_trend:*Early Insights & Customer Profiles:*
Wix Bookings & Services Consumption launched to 100% of users at the end of last week. Since then the integration has already processed over *6,837 Total Unique Bookings* and *788 Total Unique Services* :tada:
_Get to know some of our Wix Bookings Professional Services Customers!_
• <https://www.annajibeauty.com/|Anna Ji Beauty>  offers an appointment service for *Lash Lift & Tint* that has *192 bookings*
• <https://www.andradaastrology.com/|Andrada Astrology >offers an appointment service for *Returning Client Session* that has *136 bookings*
• <https://www.kimistryk.com/|Kimistry by Kim >offers an appointment service for *Alterations* that has *114 bookings*
• <https://www.mvpr.co/|MVPR Therapy >offers an *Active Recovery Class* that has *67 bookings*
:black_right_pointing_double_triangle_with_vertical_bar: *What’s Next: _Booking & Services Data Activation!_*
Wix Bookings & Services data is now available in Mailchimp’s Customer Data Platform (CDP). We look forward to continuing to partner with Mailchimp Core Product teams across: Segmentation, Audience, Automations, E-mail and Reporting & Analytics who will be leveraging these new data objects to build out Bookings based activation experiences for our customers.

:ty3: *Thank You to the following teams:*
Multi-Vertical Integrations*: <@U02KEGFKTPG|Cromwel Pestano>* *<@U085B0VAFHV|Nalin Ahuja>* *<@U031T5Y29HC|Rohit Mereddy>* *<@U0878AG7GGZ|Max Garceau>* *<@U07A05V0H5J|Stephen Komae>* 
Integrations Platform: *<@U03TDGU2JUB|Josh Day>* *<@U07GARRQRHR|Amar Manjunath>* *<@U07PNSRLYR5|Tommy Miller>* 
Architecture: *<@W8FL3AFU2|Amit Agrawal>* *<@U02KM2QGKEW|Ali Heidary>* 
Partnerships: *<@U0792U11BDX|Michael Huang>* 
Design: *<@U02KJ9QRSDT|Eddie Shrake>* *<@U05DQHZTQ3T|Jane Krause>* 
IDX: *<@U06B46M7E5N|Sunita Yadav>* *<@U049D5NR1HC|Aravind Rajendran>* *<@U065HQK3ZBQ|Somya Agarwal>* *<@U078M0WH6RH|Nirmalamary Charles>* *<@WP1J3FCSK|Arun Arunachalam>* *<@W8FMA6SUU|Ramesh Lakshmanan>* *<@W3X96BZUH|Steve Mendoza>* *<@W8FMBKWMS|Siddhartha Misra>* 
TPM: *<@U03R9TTF7FY|Abby Barnett>* 
Reactions: rocket (25), tada (19), nice-pink (6), chart_with_upwards_trend_intensifies (4), clapping-all (4), raised_hands (1), raised_hands::skin-tone-4 (1)



---

=== Message from Diana Williams (U08KK7S6LAZ) at 2025-09-09 10:41:55 PDT === 
Message TS: 1757439715.473729
Way to go team!!! Please keep me updated on performance / impact as data starts rolling in. It will be great to learn from the feedback what’s going better and what else we should do to enhance the integration for these customers.
Reactions: rocket (5)



---

=== Message from Chima Okechukwu (U03AME5740K) at 2025-09-16 08:21:00 PDT === 
Message TS: 1758036060.069429
_*#SHIP IT:*_ :green-light-siren::green-light-siren:
:rocket-launch::rocket-launch:  *Launched Personalized Experience for Switchers* :rocket-launch: :rocket-launch: 

:emailintensifies:*Executive Summary*
Today, Mailchimp uses ad hoc surveys to understand which customers are switching from other ESPs. From these surveys, we see that 44% of customers are not new to email marketing. SMS also had an in-app question that shows 25% of customers are not new to SMS marketing (link). We would like to deepen our understanding of the customers who are switching from other ESPs and activate new guidance in-app to support their transition. This is the first step on an E2E experience for switchers that will best help them migrate their data so they aren't cold starting with Mailchimp.

:jumpingstar: *What did we launch*
We updated our Features Screen and introduced a new screen to capture Switchers. For self-identified switchers, they see an updated Contacts widget on the Homepage.

Figma of the experience: <https://www.figma.com/design/PxkPgC0uEyFGNzyNmJZbfE/OBX-AS-Mid-State-Exploration?node-id=199-77748&p=f&t=amKKXhKa7zSnc5Qe-0|link>

 :shark_yay: *Analytics Insights:*
• Bayesian Chart: <https://tableau.a.intuit.com/#/site/MChimp/views/GTKMSwitchersExperiment/Story1?:iid=1&:redirect=auth|link>
 
:celebrate: *Why this is big:*
• Helps us identify switchers 
• Opportunity to drive 7D import rate
 
:hug:*What is next:*
• More personalization experiment for Switchers
*Special Shout Out:*
:clapping-1772: _*This work would not be possible without this amazing team:*_ 
• Product: <@U03AME5740K|Chima Okechukwu> <@U06QRS4SEBC|Rianna Schanno> 
• Design: <@U02104JK78A|Haemin Hwang> <@U03K5MLFBS4|Chris Sywassink> 
• Eng: <@U06PSKLD0F5|Anastasia Arnold> <@U093RNNE0MQ|Mahshid Zandian> <@U03C6DP87PF|Mostafa Derakhshan> <@U03777BQK0B|Elaine Xue> <@U060RFM8D27|Kranthi> and the awesome <!subteam^S063NQFRQSU> team
• TPM: <@U02KZTXSPTK|Erica Jones> 
• Thanks to our leaders for empowering the team: <@U08KK7S6LAZ|Diana Williams> and <@U06K8UTTSJE|Jing Wang> 
*THANK YOU*
• _For amazing work helping us identify switchers and drive their 7D import rate_
• _For an awesome collaboration_
Thread: 5 replies (latest: 2025-09-18 21:05:13 PDT)
Reactions: yes3 (2), celebrate (6), rocket_launching (3), clapclap (4), raised_hands::skin-tone-3 (1)



---

=== Message from Chima Okechukwu (U03AME5740K) at 2025-09-16 08:31:52 PDT === 
Message TS: 1758036712.082439
_*#SHIP IT:*_ :green-light-siren::green-light-siren:

:rocket-launch::rocket-launch:  *Launched SMS Cross-Sell to Non-purchase Intent Customers* :rocket-launch: :rocket-launch: 

:emailintensifies:*Executive Summary*
Roughly 15% of customers are interested in SMS early on in their customer journey. Yet, the onus has always been on these customers to find and apply for SMS before they use it. With the SMS Cross-sell experience, we have been able to bridge the gap for these customers as we introduced the SMS application right after Account Setup (<https://docs.google.com/spreadsheets/d/1jeQrJE2UHT0kRxFxopiauA_bO3NeU17YCPNFjxZFBjg/edit?gid=332925966#gid=332925966|result>). The Cross-Sell experience is currently live for purchase intent customers, and we have an opportunity to test this experience with non-purchase intent customers.

:jumpingstar: *What did we launch*
We launched the SMS Cross-sell experience to non-purchase intent customers who upgraded in Account Setup

Figma of the experience: <https://www.figma.com/design/PxkPgC0uEyFGNzyNmJZbfE/OBX-SMS-Switcher-Experience?node-id=178-71934&p=f&t=w3e696iKTqraY3jX-0|link>

 :shark_yay: *Analytics Insights:*
• Bayesian dashboard: <https://tableau.a.intuit.com/#/site/MChimp/views/GTKMSMSCrossSellExperiment/Story1?:iid=1&:redirect=auth|link>
 
:celebrate: *Why this is big:*
• Opportunity to drive SMS Attach Rate
 
:hug:*What is next:*
• Update the follow up experience for customers who do not sign up for SMS in AS
 
*Special Shout Out:*
:clapping-1772: _*This velocity and amazing turn around of the project would not be possible without this amazing team:*_ 
• Product: <@U03AME5740K|Chima Okechukwu> <@U06QRS4SEBC|Rianna Schanno> 
• Design: <@U02104JK78A|Haemin Hwang> <@U03K5MLFBS4|Chris Sywassink> 
• Eng: <@U0775UBDL3T|Vessy Shestorkina> <@U03C6DP87PF|Mostafa Derakhshan>  <@U060RFM8D27|Kranthi> and <!subteam^S063NQFRQSU> 
• TPM: <@U02KZTXSPTK|Erica Jones> 
• The awesome SMS team:<@W013E2DDP3J|Alina Rainsford> <@W8FQBKGUD|Dustin Yu> <@U03BN5DCNMT|Ruth Libowsky> <@U02KJEHK677|Neil Desai> <@U066PLZCG3B|Juan Angel> and <@U02LANRD7R6|Adam vanWestrienen> 
*THANK YOU*
• _For your awesome work to drive SMS attach_ 
• _For executing a stronger together mindset as we collaborated_
Thread: 9 replies (latest: 2025-09-16 11:27:58 PDT)
Reactions: violently-celebrating (9), nice1 (8), +1 (2), rocket_launching (2), +1::skin-tone-3 (1)
Files: SMS Cross-sell exp Results (ID: F08V38Y87QQ, application/vnd.google-apps.spreadsheet, 0 Bytes)



---

=== Message from Payton Camilli (W012EU6L7FG) at 2025-09-17 08:24:49 PDT === 
Message TS: 1758122689.107889
Here's a <https://docs.google.com/document/d/1uQaENuBogdSjm_7_u7AtY2b9XvRBDSPYRfAXZpLJVLM/edit?tab=t.0|post-launch read out> for those interested! Includes usage, learnings, and a verbatim quote from a user. Check it out!
Reactions: blob-clapping (14), raised_hands (2), raised_hands::skin-tone-4 (1), raised_hands::skin-tone-2 (1)



---

=== Message from Jacquelyn Horgan (U02KMAN6V1R) at 2025-09-18 11:00:46 PDT === 
Message TS: 1758218446.504549
*Today we're beginning the rollout of some* :glitterstars: *much needed* :glitterstars: *<https://docs.google.com/presentation/d/152AZ3Y8SLOzJ4ib0ru80PCYUPYrT0Tn5NS5WJ2LDFlQ/edit?slide=id.g372e29c550c_0_0#slide=id.g372e29c550c_0_0|enhancements to the Billing History> page.* 

*Why is this important/beneficial?*
We have _a decade_ of customer feedback on this lack of functionality, and it's fair feedback. Today, in order to retrieve a PDF receipt, a customer has to go through _4-5 clicks_ from account/billing-history to save a _single_ receipt. This receipt is clunky in formatting, with too much free space and blown out text. In order to retrieve multiple receipts, the customer has to repeat this process for each receipt, navigating back to account/billing-history each time. This is often done as part of year end book-keeping, needing to retrieve all receipts for a single calendar year. Billing Care must also go through these inefficient steps via LAU in order to retrieve receipts for users.

*What changed? [Before/after]*
:ew-gross:  2 page PDF receipt   :look-here-right: Single page PDF receipt :rapinoe-hairflip:
:ugh:  6 clicks to save a PDF receipt   :look-here-right:   1 click :boom:
:why_crying:  72 clicks to save 12 PDF receipts  :look-here-right:  1 click :boom:
:sherlock:  Scrolling/Page hopping to find a receipt  :look-here-right: Date filter :calendar:
Reactions: raised_hands (14), raised_hands::skin-tone-4 (3), rocket (12), raised_hands::skin-tone-2 (6), raised_hands::skin-tone-3 (3), yes3 (5), raised_hands::skin-tone-5 (4), clapping-all (4), yay-frog (3)



---

=== Message from Nicole Jayne (U02LB4JPAEL) at 2025-09-29 11:48:56 PDT === 
Message TS: 1759171736.196839
:rocket_launching: *Reporting & Analytics launches Conversion Insights dashboard for E-commerce ICP* :ecomm-segment:
E-commerce marketers often lack visibility into where sales are lost. As one mid-market user put it, seeing drop-offs at steps such as product viewed and add to cart is “a gold mine opportunity” to inspire new marketing approaches. The new Conversion Dashboard delivers full-funnel insights and revenue attribution, helping marketers recover missed revenue and drive higher ROI with targeted actions.

:sad-customer: *Customer problem:*
I AM a digital sales-based small/medium business
TRYING TO maximize revenue from my marketing campaigns
BUT I struggle to find opportunities to maximize conversions and get more customers through my funnel
BECAUSE Mailchimp lacks a clear picture of my customer’s journey, making it hard to identify gaps in my overall strategy
WHICH MAKES ME FEEL like Mailchimp puts the burden on me to analyze results across my program – something I rarely have time to do

:chart_with_upwards_trend_intensifies: *What was launched?*
This experiment is exposing eCommerce marketers to the new Conversion Dashboard, which includes:
• *Revenue attribution ROI:* first ever view comparing Store (e.g., Shopify) total revenue vs. Mailchimp-attributed revenue to clarify marketing ROI. All revenue data is omnichannel!
• *Shopify store funnel drop-off visibility*: See where customers fall off (page views → add to cart → checkout completed)
• *Conversion & order metrics*: 10 brand new metrics tracking impact to customers, cart size, and shopper actions
• *Guided actions & insights*: Recommendations such as recovering cart abandonment, retargeting contacts who clicked but didn’t purchase, and exploring pre-built automations
:transparent-value: *From -> To*
Siloed snippets of revenue data → Holistic Mailchimp ROI (yes, campaigns + automations!) on one dedicated Ecomm performance page
Path to purchase blind spots & lost sales → Visual path to purchase clarity & revenue recovery recommendations
Data overload, action deficit → Insights that drive action

:experiment: *What will we learn?*
This experiment will measure the impact of Conversion Insights on *increased meaningful product actions* such as segment, automation and campaign creates. Our hypothesis is that showing users actionable insights with the data visualization to back it up will lead to a reallocation of marketing to higher ROI tactics, improving share of Mailchimp attributed revenue and customer retention long term.

:next: *What’s next?*
Order attribution will significantly expand the view into Mailchimp’s ROI by automatically giving credit to brand building actions including email open and SMS delivery, as well as move the definition of “revenue” to the industry standard. To show how channels and campaigns drive attributed orders & revenue, Marketing Dashboard will get a glow up to lead with impact of omnichannel marketing on business outcome and finally include key automations performance into the total marketing impact story.

:reportingsquad: *Shout outs & HUGE THANKS*
Product: <@U02LB4JPAEL|Nicole Jayne>
Design: <@U0372SDKQDS|Tiffany Huang>
Engineering: <@U07U8BJH8R0|Manjusha> <@WAHLSUUDV|Minh Phan> <@WK626SJMC|Sudeepta Das> <@U06U846AJFJ|London Baker> <@U07B02LLNAC|Dmitri Medvedev> <@U0580HUFQ00|Scott Adams>
PMM: <@U03HRFYTYUB|Simone Kovacs>
Data Science: <@U07ED705DHS|Aastha Sehgal> <@U0970UUFN80|Ashish Prakash>
Leads: <@W8FL6URHQ|Deepak Prabhakaran> <@U02KMG1BGBV|Shane King Zackery (they/them)> <@U092280FEMP|Nitika Korla> <@W8Z8R7STE|Nir Harel> <@U02KJENBBDK|Neveen Moghazy>
Special thanks: <@U02KEEED9LN|Amit Khare> <@U04MT1U3MEJ|Caique Costa> <@W8FQBCLJH|Jake Hilborn> <@WA3PKCN66|Jessica Lin> <@U04SC218QQ3|Sijia Liu> <@U02KEQP5A6S|Wei Jia> <@U07B5L5983F|Cassandra Marshall>
Thread: 9 replies (latest: 2025-09-30 11:26:27 PDT)
Reactions: partyparrot (45), party-blob (28), omg-text (13), yes3 (12), awesome (8), rocket (10), eyes (2), clapping-all (3)
Files: Conversion insights dash loading.gif (ID: F09JL68PXDE, image/gif, 1.4 MB)



---

=== Message from Diana Williams (U08KK7S6LAZ) at 2025-09-29 12:32:36 PDT === 
Message TS: 1759174356.441889
Yes! Congratulations team!! Great work. Please share updates on performance and feedback as user engage!
Reactions: white_check_mark (2)



---

=== Message from Matt Idema (U0884DN8VGV) at 2025-09-29 13:05:36 PDT === 
Message TS: 1759176336.009829
This is a big deal congratulations team!!  Can’t wait to hear what customers think



---

=== Message from Nicole Jayne (U02LB4JPAEL) at 2025-10-14 06:00:18 PDT === 
Message TS: 1760446818.757549
:ecommerce-segment: *Reporting & Analytics enhances Ecommerce Order & Revenue Attribution* :money_with_wings:
Marketers know their campaigns drive impact, but Mailchimp’s narrow definition of attribution hasn’t always shown it. By including more touchpoints by default and aligning the definition of Revenue to Gross, we can reveal the full story of marketing performance—empowering marketers to prove value, optimize smarter, and invest their time with confidence.

:sad-customer: *Customer problem:*
I AM an Ecommerce marketer
TRYING TO understand and demonstrate the value my marketing campaigns deliver for the company
BUT the current revenue attribution in Mailchimp is limited and doesn't capture the full picture of marketing's impact
BECAUSE it excludes key touchpoints like email opens and SMS opens, has short attribution windows, and doesn't match industry standards
WHICH MAKES ME FEEL like the true ROI of my efforts isn't being recognized, and I can't make the most informed optimization decisions.

:chart_with_upwards_trend: *What was launched? From -> To*
This release introduces a fully modernized, CDP-backed, and scalable service, building on the Integration team’s earlier work to bring Attribution in-house and provide customers with customization settings. New enhancements include:
• *New attribution defaults:* From default settings that ignore the impact of opens -> New attribution defaults that give credit to brand building activities
• *Reattribution*: From customization that only impacts activity from that point forward -> back calculating the last two years of data for consistent historical reporting
• *Gross Revenue*: From subtracting tax & shipping from revenue totals -> aligning to the industry standard use of Gross revenue 
:product-insights: *What will we learn?*
This launch will measure the impact of these changes on the average share of attributed revenue (currently 14%!), the perceived accuracy of revenue attribution metrics and the number of new bookings & retention of Ecommerce customers. Early indicators of satisfaction will likely be seen in the share of customers who customize their attribution settings remaining low. A pre-release measurement of perceived accuracy found 49% trusted attribution settings, and post release sampling will watch that number closely for improvement.

:next: *What’s next?*
Ecommerce marketers will gain additional insight into how marketing is driving C2 consideration with new attribution of site activity collected from Shopify S2S and a future Mailchimp pixel back to campaigns. To serve Professional and Retail Services ICPs, attribution will be expanded to report on Bookings and Payments (including Quickbooks!) conversion events. And as Mailchimp rolls out new channels including Whatsapp and RCS, they will be onboarded to this new attribution service.

:highfive3: *Very well deserved shout outs!*
Product: <@U02LB4JPAEL|Nicole Jayne>
Engineering: <@W01108SHDV4|Sarvesh Kumar> <@U02K6FKBG31|Benjy Phillips> <@U03SZ30NENB|Jonathan Davis> <@U046WDQCP0R|Cavin Myers> <@U04EWBQLUJE|Richard Do> <@U03ALF0U1GR|Carson Britt> <@WAHLSUUDV|Minh Phan> <@U071H9QQZ7F|Alexandria Cassagnol> <@WK626SJMC|Sudeepta Das> <@U02KMECQYRY|Paco Orozco> <@U06U846AJFJ|London Baker>
Design: <@U0372SDKQDS|Tiffany Huang>
PMM: <@U03HRFYTYUB|Simone Kovacs>
TPM: <@WP0ENL12Q|Deepak Mirani>
Data science: <@U07ED705DHS|Aastha Sehgal> <@U0970UUFN80|Ashish Prakash>
Data eng: <@U02LAV55V40|DeAnna Rushing>
VOC tracking: <@U02K6PV38NT|Rob Adair> <@U02KJ5KSGUV|Bri Estolano>
Leadership: <@W8FL6URHQ|Deepak Prabhakaran> <@U02KMG1BGBV|Shane King Zackery (they/them)> <@W8Z8R7STE|Nir Harel> <@W8FHXCZSP|Saikat Mukherjee> <@U02KJENBBDK|Neveen Moghazy>
Thread: 6 replies (latest: 2025-10-14 13:21:57 PDT)
Reactions: party-blob (28), clap-blob (14), joe_lfg (7), muscle (6), raised_hands (4), money-bag (3), muscle::skin-tone-4 (1)
Files: Revenue notice.png (ID: F09KUR1JT3R, image/png, 357.7 KB)



---

=== Message from Elizabeth Bertasi (U06QWR7FV9T) at 2025-10-14 09:22:24 PDT === 
Message TS: 1760458944.340109
:rocket: :cjb: :new: *New automations homepage experience launched!*

:search-pin: *What’s new?* 
We released our new automations page structure to personalize the automations experience and increase automations adoption, after a 4-week bayesian experiment. This new homepage introduces key help content for new users, an easy getting-starting checklist that is personalized by industry, and streamlined navigation, especially for users already familiar with automations.

:analytics-graph: *Impact & metrics:*
Variant traded off some top-of-funnel creation, especially among FTUs, but delivered stronger downstream conversion, ultimately netting neutral Turn On rate.
• Top of funnel softened: create among FTUs is notably down. 
• Strong downstream lift: Journey Create → Turn On Rate in the variant is substantially up among FTUs, indicating that FTU creators in the variant were higher-intent and/or better informed.
• Cross-sell impact minimal: SMS registration, integrations creation, and form creation were all flat.
:coming-soon-icon: *What's next?* 
We'll iterate on what we've learned, pushing farther into personalization and ICP value. Stay tuned!

:clap: :clap: *Shout outs:* 
Thanks to the brilliant and talented automations team that made this release possible!
<@U02KJ1UDHC5|Bobby Craig> <@U02KZQKLPR7|Chris Pitts> <@U03GVFDGUKA|Cliff Martin> <@U03GE2Y59M0|Dana Winn (Automations Oncall)>  <@U02KZU660AV|Jameson Brown> <@U02KMC0QGSW|Justin E. Samuels> <@U02KMDU1TU2|Maxwell Reich> <@U02KMGM5D98|Yena Ku (they-them)><@U07UCSZSA30|Keith Ferney>  <@U05E0NM781H|Aliyah Owens> <@U063VQYDNQ5|Livia Gimenes> <@U0511DNU1NF|Mikey Kambli> <@U07UDRJAAF3|Regina Donovan> <@U07UY6KBVNV|Rob Berryhill> <@U07NA0QPYJ0|Saisharath Peddibotla>
 <@U02KMBNL2UB|Jena Powell> <@U02P9STSQGZ|Becca Walsh> <@U02KZMX4E6M|Celeste Mora (they/them)> <@U02KMBDS7AP|Heather Dartz> <@U06QRS4SEBC|Rianna Schanno> <@U07AX5J7MFB|Eric Anderson> <@U03FRS5AGAU|Rubi Gutierrez> <@U07RKQ1P8Q2|Yizhou Qiu>

*Resources*:
<https://docs.google.com/document/d/1FRfFpP9tN69qnbaN0YV8JxXhj2dgqQgVHXEtiLFmTyQ/edit?tab=t.0#heading=h.o8l4kdkqw480|PRD>
<https://www.figma.com/design/ay6svUdv2Qsnx70bQPFbZq/CJB-%E2%80%94-Squad-work-FY25?node-id=11501-415876&t=Y78m5PQotxcKrdpN-0|Figma>
<https://docs.google.com/document/d/123RUtVtc2W5z1L3U18WbpdG5lLe9ieuDKQhffd-lP-M/edit?tab=t.0#heading=h.4c40og9ra3k3|EDD>
<https://docs.google.com/presentation/d/1mFdj72KJK53cheWe4-rSrvWKBQTrQP3S9ymP5kAplHo/edit?slide=id.g383e51582e9_0_18#slide=id.g383e51582e9_0_18|Bayesian test result readout> (and from/to of the experience)
Thread: 1 replies (latest: 2025-10-14 10:15:54 PDT)
Reactions: celebrate (17), awyea (9), yay (7), clapping-all (11), pandadance (6)



---

=== Message from Matt Idema (U0884DN8VGV) at 2025-10-14 10:14:44 PDT === 
Message TS: 1760462084.179849
BOOM!! :firecracker:

Congratulations team this is a biggie and I know you all worked really hard to get this out with quality!

Excited to hear how customers feel about this one and the rest of our eComm launches this week!
Reactions: thank_you_ty (10)



---

=== Message from Alina Rainsford (W013E2DDP3J) at 2025-10-14 12:01:22 PDT === 
Message TS: 1760468482.235489
*Launched: Multi-country SMS sending and Multiple SMS enabled audiences*  :rocket::earth_americas::trophy:

Over the past year, we’ve grown our paid SMS users by 83%, doubled our revenue, expanded to 12 countries, and introduced tons of new features.  All of that amazing growth came even though our customers had to choose _one country_ and _one audience_ for their SMS campaigns.

Today, we’ve hit a huge milestone in our SMS product and removed that limitation! A customer can now register and send SMS to all 12 countries on any audience. We’ve also *introduced a new revenue line* - charging for multiple phone numbers in an account.

Multi-country SMS sending has consistently been the top request from our EMEA sales teams and closes a key competitive gap with Klaviyo and Attentive, and multi-audience has been a key feature request from mid-market sales teams. In fact, multi-audience is a differentiating feature for us. In our competitors, these customers would need to maintain multiple accounts, but we allow them to do it all under one Mailchimp account compliantly. As part of this release, we also launched the ability for a C1 to “send to multiple segments” - an important feature in Email that had been missing from SMS!

This project was a _*ginormous*_ undertaking that spanned *nearly every product development team at Mailchimp*, involved flipping our SMS and Audience architecture on its head, wading through a ton of complexity to account for the many permutations a customer could be in, and was completed *in under 2 months*.
I’d like to especially call out <@U03BN5DCNMT|Ruth Libowsky> who architected this massive change to our product in record time, and <@U03J3GGU5T3|Jeremey Nofzinger> for his boundaryless leadership:clapping-all:

Thank you to all of the teams who worked late nights, weekends and holidays to deliver this highly complex release in under 2 months!  Thank you to our GTM partners who helped us get here and make this a success at launch. For more information, check out the <https://intuit.seismic.com/app?ContentId=fe586773-ee4d-440e-a4db-01abce66dee0#/doccenter/db3a1e99-148a-4e2d-8621-32e807774f10/doc/%252Fdd55e7fcfa-8f0f-4cc5-918e-d7fd4614be17%252Flf4a61882c-9bc3-4c10-bee0-9906ae5b2b99/grid/|seismic hub>, and we’ll follow up with release tracking shortly.  We've already seen a *$37K MRR Spain account purchase 5 additional numbers,* and our largest SMS customer in the UK purchase an additional number.

:cheerss: With that, thank you to the massive village of folks who rallied around this project to deliver for our customers in time for peak season!

Messaging: <@W013E2DDP3J|Alina Rainsford> <@U076PQ83WPJ|Ana Bell> <@U03BN5DCNMT|Ruth Libowsky> <@U03J3GGU5T3|Jeremey Nofzinger> <@U03NU55364D|Satish Sambandham> <@U0946BZ3QTW|Mike O'Dell> <@U02KPE15PCL|Connor Callahan> <@U02KEJR5LP8|Jeremiah Edmond> <@U02KJEHK677|Neil Desai> <@U02KM1TUH8B|Ashley Lawrence> <@U02K6LEHGKZ|JB Lovell> <@W8FQBKGUD|Dustin Yu> <@U03V70QRTRQ|Mythili Gopikanth> <@U02KJF76MU5|Rujuta Apte> <@U02KMCPHWAX|Laura Celentano> <@U03TDLSFYH0|Ben Marks> <@W0133SBDGCA|Chung (Chunghee) Kim> <@U03LTUC0RA8|Abhishek Salve> <@U02LANRD7R6|Adam vanWestrienen> <@U06N722QGP3|Anila Mada> <@U02KJ9AN5FF|Christian Blades> <@U02KPENAJ0L|Chris Whyte> <@U06B9T6B1RP|Christian Gaviria> <@U05GSV3QRHC|Daimen Williams> <@U06D0QM9L1F|James Dominic> <@U066PLZCG3B|Juan Angel> <@U06T2RV3755|Jyothi Karlapudi> <@U06QHNDKYQK|Leo Lin> <@U04UXHWUGHL|Ricky Amparo> <@U03QV7NC05P|Pavlo Lyalyutskyy> <@U06DNT6E69F|Swanand Patil> <@U0703THQZRQ|Gary Aloisio> <@U094R1RP1D5|Charles Hall> <@U07LPMM9HL6|Chintan Patel> <@U04V3NDEVC2|Krishna Desai> <@U03TAMM16LV|Rick Barker>  <@U03BZ61PHTK|Ryan Tay> <@U04739FF7M5|Adam Williams> <@U0970UUFN80|Ashish Prakash> <@U02724E1DFB|Jeremy Diaz> <@U06UQL9V07R|Himanshu Dubey> <@U02LB276CMN|Jonathan Hunsucker> <@U07S4GH0JT1|Pascal Allen> <@U04QZ1RRPLN|Ty Kuhn> <@U02KJBP43V3|Jess Riddle (She/Her)>
Audience: <@W012EU6L7FG|Payton Camilli> <@U07TBG84162|Andres Botero> <@U02KZQ945CH|Carlton Freeman> <@U03A74N8Q23|Dylan Corbett> <@U02KEJS1A3Y|Jay Sun> <@U035UM0LKDJ|John Wozniak (ON-CALL)> <@W8Q97P0AE|Josh Tate> <@U03TDL2C5HQ|Matthew Marberry> <@U02K9LARL4S|Tara Felzien> <@U07USKD0MA5|Shefali Dalal> <@U035AGFSBRC|Sabrina Harris> <@W019Y5V05UG|Mohammad Habbab> <@W8FHXCZSP|Saikat Mukherjee>
PLC: <@U02KZSQSXAM|Curt Shearer> <@U045QK7AM1A|Anesia Smith> <@U05NALW1S3U|Collins Amadi> <@U02KJF38AAZ|Patrick McKinnon> <@U03CJLQEUCF|Remya K> <@U047HMUGE82|Erin Szarpa> <@U02KM9USVDY|Greg Clark> <@U07PV9VL1HD|Omar Carrasco><@U07MYEG53JB|Rhomaro Tesfai-Powell>
Automations: <@U06QWR7FV9T|Elizabeth Bertasi> <@U02KMBDS7AP|Heather Dartz> <@U03GE2Y59M0|Dana Winn (Automations Oncall)> <@U02KM32BC67|Alejandra Rodriguez> <@U02KMC0QGSW|Justin E. Samuels> <@U02KMDU1TU2|Maxwell Reich> <@U07UDRJAAF3|Regina Donovan> <@U07UY6KBVNV|Rob Berryhill> <@U02P9STSQGZ|Becca Walsh> <@U02KMBNL2UB|Jena Powell>
Forms: <@U0792LBEN86|Giorgos Papadimitriou> <@U07996KNNPM|Evangelos Rigopoulos> <@U06QZKUP142|Sean Fleming> <@U06K1M3KGHZ|Laura Guillen> <@U02KME26NUB|Michael Pazinets> <@U02MG4JS7K9|Aum Dutta>
Segmentation: <@U03KUBTCSG1|Frank Persico> <@U075WV52TQS|Nick Horvath> <@U04TWCYUZAN|Mason Hadeler> <@U05KZB08WRY|Jon Griffin> <@U07Q70L7BC5|Vova (Vladimir) Shechtman>
CDP: <@U0789R246JY|Leila Jalali> <@W8FQBCLJH|Jake Hilborn>
OBX: <@U02KM90H7R9|Brittney Muhamed> <@U0428EDN518|Nick Boyle> <@U02TP8JFQ4Q|Chris Keimig> <@U03EEL3PU9H|Sid Kumar> <@U02KZTXSPTK|Erica Jones>
QA: <@U03DJNFKW4T|Nicole Robinson> <@U02KM87A7SN|Brittany Tims> <@U02KEQP5A6S|Wei Jia> <@U02KJ5X1V3P|Cary Duncan> <@U02KPLAS31S|Mike Walker> <@U02KMCPHWAX|Laura Celentano>
R&A: <@U05AMM7NF5J|Taylor Mattson> <@U071H9QQZ7F|Alexandria Cassagnol> <@U081SRZEGUE|Andy Nguyen> <@U03ALF0U1GR|Carson Britt> <@U07B02LLNAC|Dmitri Medvedev> <@U03SZ30NENB|Jonathan Davis> <@U092280FEMP|Nitika Korla><@U092PTWA2V9|Ramon Ramirez> <@W01108SHDV4|Sarvesh Kumar> <@U02KMG1BGBV|Shane King Zackery (they/them)> <@WK626SJMC|Sudeepta Das> <@U02L04W0FPT|Tamlin Tromp> <@WP0ENL12Q|Deepak Mirani>
Legal: <@U04FF36UREJ|Lina Lozano Oviedo> <@U04D5LZ3KFC|Jasmine Lowe> <@U07Q0RN0C5S|Renee Moore>
Marketing: <@U02KEQJS3LN|Wade Burrell> <@U096X02TTP0|Kendall Kautz> <@U096DLJK8NA|Jonathan Rodgers> <@U04G5KNNVUM|Katie Witkowski> <@U03UPFR5PB5|Sarah Mullins> <@U0776PKRVP1|Brittany Morrow> <@U0211NGN163|Shuaiyu Guo>
Rev Ops: <@U07EFT25CBB|Stuart Chuang> <@U0664FD1LTZ|Rohan Thakur> <@U07SF0TTRM5|Paul Kundel>
FDTG: <@U02TNUQ1868|Srinivas Manepalli> <@U05UKT1MY1Y|Saumil Thakkar>
Finance: <@U02KEHK13FG|Daniel Varela> <@U02KMDEB5GS|Llewellyn Berg> <@U087ALUMJ8N|Chang Park>
Revenue Recognition: <@U05QNVD0KHP|Cuc Le> <@U02724E1DFB|Jeremy Diaz> <@W8FMB5WKW|Barb Magner>
CSM: <@U02Q5TAER1R|Jordan Castelan> <@U07F91F200Y|Kristi Donahue> <@U078P6S0S5D|Savannah Williamson> <@U07F2TB4Q1K|Sunali Bhandula> <@U060NKPDHF1|Swati Bala Subramanian>
GTM PMO: <@U037ZE99WC9|Madaline Goldstein>
HA Enablement: <@U02M49MR0TX|Celia Shore> <@U02KEFCR26A|Craig Goldberg> <@U084ZTZF15E|Faye Harris> <@U040F42EC69|Haley Dutton> <@U02KMBFM9PU|June Lee>
Sales: <@U01EJP04Y93|Aisha Schenk> <@U02KEQX6894|Vinny Ferro> <@U07PSP1P2PL|David Koeppel><@U02KPJDJ3N0|Kavita Mani><@U05LMA1PUCR|Miriam John>
SolCon: <@U02LB0ECVR6|Eric Cash> <@U02MUGRUS79|Lina Rodrigo>
Web: <@W9GLZQ45A|Ryan Tuosto> <@U06GGQHJT9N|Jim Mccaffery>, Amber Gordon <@U033CC0AUD8|Caroline Josey>
Compliance: <@U02KMGR6XSP|Tristan Loebker-Connelly>
Trust & Safety: <@U02LAV5UQQ0|Blair Sullivan> <@U02CJJ8MM6G|Kim Gurvitz> <@U07CPLXBGB1|Karthi Subramanian> <@U059N17HQLD|Anuradha Gudapati>
Technical content: <@U098R1R6E2U|Lakita Backum> <@U02KPDF0CSY|Cheryl McCurdy>

And thanks to our leaders for unblocking us at every point along the way! <@U08KK7S6LAZ|Diana Williams> <@W8FHYGK19|Jack Tam> <@U07AX5J7MFB|Eric Anderson> <@W8FQBMAN9|Andrew Firstenberger> <@U02KJEHK677|Neil Desai> <@U02KJF76MU5|Rujuta Apte> <@U03NU55364D|Satish Sambandham>
Thread: 12 replies (latest: 2025-12-04 10:22:24 PST)
Reactions: party-blob (97), yay (53), celebrate (45), cat-clap (28), blob-dance (30), amazing45 (25), clap-blob (19), joe_lfg (17), rocket (24), nod-redford (13), awesome (15), fire (15), star-struck (11), spinning_globe (9), audience (8), blob_cat_sms_intensifies (5), mr-worldwide-pitbull (5), raised_hands (6), raised_hands::skin-tone-2 (2), raised_hands::skin-tone-4 (1), mc-sms (2), raised_hands::skin-tone-6 (1), lets_go (1), extreme-teamwork (1), go-team-667 (1)



---

=== Message from Matt Idema (U0884DN8VGV) at 2025-10-14 13:47:04 PDT === 
Message TS: 1760474824.777959
WOW WHAT A DAY!!!  Congratulations team..  I know we pre-celebrated a bit last week but it's much cooler when the code is live :sunglasses:

Great work this has been one our customers have been asking for excited to see them all use it!`
Reactions: clap-blob (28), teamwork11 (11), heart (4), ty3 (2)



---

=== Message from Adam Anger (U054QGJRYJF) at 2025-10-14 19:56:27 PDT === 
Message TS: 1760496987.172179
Big congrats!! Exciting milestones today to get some of these much needed features into the hands of our new and existing customers!
Reactions: celebrate (4)



---

=== Message from Joshua Fischer (U07RNSH0256) at 2025-10-15 10:34:54 PDT === 
Message TS: 1760549694.044649
*<https://us14.admin.mailchimp.com/templates|New Template Gallery >Tab Launched* :win:

*TL;DR Payoff Rate - the <https://docs.google.com/presentation/d/1D-S0hQcRSCDt528vbSdSr44myZwIDdtZzjlzbj4i88Y/edit?usp=sharing|leading indicator for 90D retention and revenue>* - *saw increases of +4.7% (v1 stat sig) for New Customers and +0.5% (v2 stat sig) for All Customers with the new Email Template Gallery.*
*The Gallery adds visibility for our prebuilt template designs, which led existing customers to create and send more new designs and fewer saved/replicated or from scratch templates.*

*Customer Problem: I am* looking to save time on my next email by starting from a template, *but* it’s hard to find templates that meet my industry, business style, and email intent.

*What was launched?* (see before/after screenshots below):

*Previous Experience:* Templates tab was under Content Heading and contained only Saved templates
*<https://us14.admin.mailchimp.com/templates|New Experience>:* Templates tab moved up under Campaigns heading and new design that contains: Mailchimp Designs, Saved & Recently Sent
• Variant 1 (V1): Default to All Mailchimp Templates tab
• Variant 2 (V2): Default to Saved Templates tab IFF customer has saved templates
*What was the impact?*

We saw an increase in overall campaigns created on Mailchimp with more people sending basic (stat sig) and predesigned (directional) templates and fewer sending replicated, Start from Scratch or - surprisingly - Saved Templates.  Total sends were flat, meaning that overall C2S rate actually decreased for the variant vs the control.  HOWEVER,

Our primary metric of *e*mail payoffs (# of people who send ANY emails to 10+ contacts) *was up 0.5% for all customers* (51.72% to 51.98%), and *for New Mailchimpers payoffs were up 4.7%* (stat sig) for V1 and 4.4% (directional/not stat sig)  for V2 (10.11%C to 10.59%V1 to 10.56%V2).

*What's our Interpretation?*

People in the variants were more likely to discover new template designs (or even find them at all) in this more visible experience.  So this treatment empowered more customers to create campaigns with new designs, rather than using saved or replicated ones they have used previously.  This had an outsized impact on *new customers now being able to find ANY template to create and send their first email*, which we know is a BIG DEAL to get them to stay with Mailchimp.

*Next Steps*

We rolled out variant 2 (default to saved) to everyone as it had a significantly positive effect on payoffs overall, despite being .03% lower for New User payoffs which made it not stat sig, but directionally similar.  Overall the experience, especially for new customers, was very similar.

Continue reviewing this new experience and try to ameliorate the C2S drop by ensuring customers are able to find the kinds of templates they will want to send and will make them successful.  We also saw a drop in C2 open and click rates, so making sure customers are successful when they select new templates is critical as we continue to iterate.

Major Kudos to the team who spent a lot of time making this a reality
Design: <@U02MR1GFZRN|Wynne Leung> <@U02KMCWL9LJ|Madeleine Stein><@U02KJA0C137|Erin McCue>
Engineering: <@U07LPMM9HL6|Chintan Patel> <@U02KM7S28TU|Craig Rodrigues><@U02KZSVL75F|Christina King> <@U02KMDVUEUT|Mike Murray> <@U0946BZ3QTW|Mike O'Dell><@U02K6LEHGKZ|JB Lovell>
Data: <@U055LGZB276|Brian Fong><@U02QFTEHKB9|Kevin Martin>
TPM: <@U02KJ5X1V3P|Cary Duncan><@U02K6LY0X63|Jessie Brown>
Product: Nabil Mastan
Thread: 2 replies (latest: 2025-10-15 11:31:48 PDT)
Reactions: build_it (11), clapclap (19), bananadance (5)
Files: image.png (ID: F09LKHEDU1W, image/png, 105.4 KB), image.png (ID: F09KRG9JMHQ, image/png, 574.0 KB)



---

=== Message from Matt Idema (U0884DN8VGV) at 2025-10-15 10:43:31 PDT === 
Message TS: 1760550211.259589
Solid win..  nice work team!
Reactions: raised_hands (1), raised_hands::skin-tone-3 (1)



---

=== Message from Halil Kiper (U07SMNM5RHA) at 2025-10-21 07:14:59 PDT === 
Message TS: 1761056099.231669
:rocket_launching:Launched - *ICP determination for FTUs*:rocket_launching:

*Title/release name:* 
Enable Personalized Experiences by ICP for FTUs across Mailchimp.

*Overview:* 
Want to personalize the Mailchimp experience based on their ICP or C1 Attributes? Now you can! The team launched 2 MSaaS Services completely built on Intuit Tech ecosystem that provide the near-real time access to WHO the customer is; both explicitly provided by the customer or derived from external sources (i.e. Webscrape, AI Inferences, ZoomInfo).

The <https://devportal.intuit.com/app/dp/capability/APP-0093/api-reference/rest/NDcyNw/v1determineicpPOST|getICP endpoint> provides ICP information for C1s who enter their website url during Account Setup. It uses <https://docs.google.com/spreadsheets/d/1c1bQKerCyg2ZjmcDuLzru-mIqgjjlSLyfH3thPcwyG4/edit?gid=691655386#gid=691655386|11 different customer attributes> to derive the ICP that can be used to tailor features and recommendations that you all build.

*Engineers:* Integrate with a simple, reliable API built on our own stack. No external dependencies, just fast, clean data. No need to call ZoomInfo separately.

*Product Managers:* This is your tool to power personalized done-for-you experiences for customers.
• Create dynamic  flows tailored to specific verticals.
• Power targeted features  for an ICP segment.
• Deliver smarter in-app messaging that speaks your customer's language.
• Finally, unlock the deep C1 understanding you've been asking for.
*What’s next:*
Phase 3 of ICP Identification (GA start: 11/12/25)
• Tenured user ICP determination and making it available to all services
• Refresh Marketing Vertical and ICP labels and sync with BQ table
• At this point, we will have full coverage for both tenured and FTUs via the getICP endpoint for downstream apps and BQ tables for analytics. 
*Impact & metrics:*
• Check out a sample <https://docs.google.com/spreadsheets/d/1S1hdbsHW7EnxuxNNLRf5lZsN9IWiEV4WrHtjlMGbS4M/edit?usp=sharing|here> and <https://drive.google.com/file/d/1MqdvXINYE5mROTFPgCpqi7v5dtwX_RHN/view?usp=sharing|API response>.
• High level stats since launches of Phase 1 in August and Phase 2 in Oct: Total of 12.6K FTUs (to date) and ~1M active tenured users have been classified:
    ◦ Professional Service: 40%
    ◦ DSB (Digital based omnichannel + ecomm): 22% (but 32% have online stores)
    ◦ Community based non-profit & edu: 13%
    ◦ Community based ent & leisure: 6%
    ◦ Subscription based B2C SaasS: 2%
    ◦ Subscription based content: 2%
*Gratitude/shout outs:* 
Major co-creation from <@U02LB4JPAEL|Nicole Jayne> <@U02KJ15KCA1|Brooke Hatfield (she/her)>
TPMO: <@U02KZTXSPTK|Erica Jones>
OBX Engineering: <@U060RFM8D27|Kranthi>  <@U07PB187TCJ|Oksana Yarosh>  <@U063JM5UW5P|Alex Vovk>  <@W8FQB94DB|Ravi Channapati> <@U08T0KH4Q3D|Sripriya T> <@U093H8QD9H6|Vikram Reddy Chintalapuri> <@U03C6DP87PF|Mostafa Derakhshan> <@WRHEEP39A|Mehrshad Sahebsara>
Brand Engine/Webscrape Engineering: <@U02KMCXQJ7M|Kelly Hale> <@U074WR8A48H|Chris Lansing>
ML Engineering: <@W8F0QJHR6|WeiFeng Zhang>
Data Engineering: <@U078EQTQFRP|Pankaj Bhatia>  Jessica Rudd
AI Science:   <@U060R5W9QLA|Skanda Vivek>  Ash Griffin <@U0793KXBF51|Bryan Smith>
DSB:  <@U02K6PULZQX|Pooja Berrong> <@U086MMX7W0M|Juliana Simoes> <@U079SMT5UTA|Matt Cimino>
Leadership: <@U06QRS4SEBC|Rianna Schanno>  <@W8GN4BUBH|Danh Dang> <@U06K8UTTSJE|Jing Wang>
Product: <@U07SMNM5RHA|Halil Kiper>

*Resources*
<https://docs.google.com/document/d/1ioYp18QfdtvkV1W7gdmQFuJo-u3wx7SFg1NGa2q16BI/edit?tab=t.0|PRD>
<https://mailchimp.splunk.intuit.com/en-US/app/search/mailchimp_ideal_customer_profile_service/edit?form.global_time.earliest=-24h%40h&form.global_time.latest=now|Result Tracking>
<https://wiki.intuit.com/pages/viewpage.action?pageId=1447259716|Rollout plan>
<https://docs.google.com/spreadsheets/d/1c1bQKerCyg2ZjmcDuLzru-mIqgjjlSLyfH3thPcwyG4/edit?gid=691655386#gid=691655386|Marketing Vertical/Industry Taxonomy Definitions>
<https://docs.google.com/spreadsheets/d/1c1bQKerCyg2ZjmcDuLzru-mIqgjjlSLyfH3thPcwyG4/edit?gid=958165828#gid=958165828|ICP designation logic>
<https://docs.google.com/document/d/1ioYp18QfdtvkV1W7gdmQFuJo-u3wx7SFg1NGa2q16BI/edit?tab=t.0#bookmark=id.8fjv775wjvp4|BI Table with already labeled ~1M users>
<https://devportal.intuit.com/app/dp/capability/APP-0093/api-reference/rest/NTE0Mw|getICP API documentation >and <https://drive.google.com/file/d/1MqdvXINYE5mROTFPgCpqi7v5dtwX_RHN/view?usp=sharing|sample response>
Thread: 10 replies (latest: 2025-10-21 11:00:22 PDT)
Reactions: highfivefey (7), clapping-all (15), tada (9), 100 (6), winning-kid (3), teamwork1-nb (4)



---

=== Message from Elena Simon (U02KPFWHRU4) at 2025-10-21 08:36:54 PDT === 
Message TS: 1761061014.119789
:rocket: *Mailchimp and One Intuit Account: Unified Identity is now unlocked!!* :rocket:

:rocket-party: *What we launched:*
Quickbooks and Mailchimp customers who sign up for Mailchimp from the <https://quickbooks.intuit.com/mailchimp/|Simulated Bundles> flow on <http://QuickBooks.com|QuickBooks.com>, or the <https://docs.google.com/presentation/d/1dKDM469F8BPeq0gC3Yg8ISpuBsDBSGp9pQhDyHNTHG0/edit?slide=id.g34fbcbe0af7_0_37#slide=id.g34fbcbe0af7_0_37|Marketing page inside of QBO> can now reap the benefits of the Intuit platform and manage their business in one place! These customers can use <https://docs.google.com/presentation/d/1M3c5Ect6ddyRZyEHYbpC4ducv_tgW6cZUovsv65jl4o/edit?slide=id.g329e0aea6b4_0_3848#slide=id.g329e0aea6b4_0_3848|one Intuit credential across QuickBooks and Mailchimp>, eliminating the need for separate logins for each platform. This marks a critical milestone for Intuit and Mailchimp in our mission to deliver a truly unified and deeply connected experience for all small businesses.

:bar_chart: *Early data*
We’ve seen *400+* new MC customers take advantage of these offers through these updated user experiences, improving the *seamless* *account creation success rate from* *42% to 53% (127 ITP)* with extra steps removed, *100% seamless login success* between QB and Mailchimp in a single click, and *20-26% converting to paid MC accounts*. Funnel improvements also include an increase from *64% to 89% email activation success (139 ITC)* and *GTKM start rate from* *56% to 78% (139 ITC)* . Customer engagement with a new Unified User Management (UUM) experience between Mailchimp and Quickbooks is also trending above forecast with a *71% add user success rate* and above target *76%+ invitation acceptance rate*! This first milestone gets us closer to our goal of enabling 100% of New and Existing QBO Customers to be eligible to seamlessly create Mailchimp accounts via Identity from <http://QuickBooks.com|QuickBooks.com>. (<https://docs.google.com/presentation/d/1m1QiAaAiXAXvSnnrnlmx9VG7BVskhrKL66KM5QkcVT4/edit?slide=id.g31def94eee5_10_1#slide=id.g31def94eee5_10_1|Reference>)

:ty_thankyou: *Shout outs* to the incredible organizations and teams that made this possible:
*`Mailchimp`*
*Identity -* <@W8FL2R1J6|Roopesh Sheth> <@W8FQB94DB|Ravi Channapati> <@W8FQCNZSR|Gayathri Muthukrishnan> <@W8FHX8G9Z|Bimal Manukonda> <@U03CH434152|Varun Murthy> <@U06A00N0DG8|Ketan Barve> <@U03NX2Q881G|Sasivardhan Reddy Mamidigumpula (sasi)> <@W8QGZ051C|Srinivas Jakka> <@U03K8JT4V5X|Sravya Jarugu> <@W013Z8Z7ZH9|Pavithra> <@U06MTKVBPME|Moulika> <@U062F21S611|Amy Hao Luo> <@U07GEQUL0GL|Meet Parikh> <@U035H6678PM|Sharad Srivastava> ,  *Billing:* <@U03A50JQBA9|Shasikala Papisetty> <@WGVNFKU13|Truc Nguyen> <@U088089HFJ7|Brahma Narayanan> <@U02KJF38AAZ|Patrick McKinnon> *Data Science -* <@W8F0RNH4Y|Nathan Bullock> <@U03A5T1UH4M|Matthew Hendler>, *Data Engineering* - <@U05A4D12BT8|Alexandra Pappas> <@U02K6M6M2AK|Kale Davis> <@U078EQTQFRP|Pankaj Bhatia> <@U05B8V54DC0|Rich Archer> <@U02LB440SGG|Nathan Hoffman> <@U07GLH2MT32|Alex Malokin>, *Risk -* <@U02KMEYPJJX|Nigel Brown> <@U02LAV5UQQ0|Blair Sullivan> <@U059N17HQLD|Anuradha Gudapati>, *Marketing -* <@U02KM9R6R8A|Danielle DeSarzant>, *Digital Delivery -* <@U02ME1MUHDY|Joy Todaro>, *QA -* <@U02KZQW6AG1|Amber Lawson> <@U02KM4DAT6W|Alison Seto> <@U02LB3PKAHW|Matt Castilla> <@U02KEED6LTG|Ankur Bag> *Product -* <https://intuit.enterprise.slack.com/team/U02KEJKU6NS|Jamillia Brewington> <@U06QRS4SEBC|Rianna Schanno> <@U02KJDT7YMT|Margarita Caraballo> <@U02KPFWHRU4|Elena Simon>, *XD -* <https://intuit.enterprise.slack.com/team/U02LQKJEC8N|LJ Jackson> <@U03K5MLFBS4|Chris Sywassink> <@U02KPLF0PPW|Molly Hoffmeister> <@U02KPCDC752|Aparna Somvanshi> <@U02TP8JFQ4Q|Chris Keimig>,  *PMO -* <@U02KEEE7V8E|Chanel Hicks> <@U02KMDCS7PD|Lauren Ebrahim> <@U02KEKMTNNA|Jenn Reed>
*`Intuit Identity`*
*IDLM -*<@U030JN0K1GS|Aasif Mohammad> <@W8GG77ALE|Raymond Chan> <@W8FHX0143|Jeff Geisler> <@U0215C8AEV9|Shalima Sidhik (she/her)> <@U01SWLAGF0X|Dmitry Ivanov>,  *AuthN -* <@W8FL3PAE6|David LeRoy> <@W8FHYFLAX|Sarah Nakao> <@WTH67L4M8|Jordan Nova>, *AuthZ -* <@W8FQC4WQ5|Randhir Sinha> <@W8FQBLE93|Raghavendra SC> <@WQ09KSECX|Ritika Raj> <@WKJ23707N|SUBHARTHI KUNDU> <@U026CD147L7|Siddharth Chaudhary> <@U055A55NF36|Shyamal Jain> <@U02U97Y9VDL|Diksha Shrivastava>, *CI -* <https://intuit.enterprise.slack.com/team/W8FQBCUS1|Dhivya Arumugam> <@U02JVN25YJ0|Manish Kumar Singh> <@U04D64BNE5N|Mohit Kumar> <@U054FLMHJ6L|Sankalp Ranjan> <@U03PSFEQ98T|Pragya Agarwal> <@U06AENFKSL8|Preetom Bhowmik> <@U056XN8PLSE|Gauri Mishra> <@W8F0S7KNU|Sivaraman Sathyamurthy> <@WEWTZ8RUZ|Avinash Tiwari> <@W8GG81G5U|Vijay Kamath>, *Consent -* <@U0289GJ9VUP|Raunak Bagri> *Data Science -* <@WB94SE80H|Samantha Akers (She/Her)> <@W8FQCPKHT|Swathi Chandrasekar> <@U01P4SUSWQP|Shashank Darisi>, *Product -* <@W8F0R1A7J|Katie Wahlman> <@W8PPAEFC1|Priscilla Hawkins> <@U08HNQ5QC15|Anand Yadav> <@W8FM9G85S|Amit Bhatia> <@U03BF72T5K7|Ahila> <@U03CHRCTUH5|Amit Arora> <@U03QYHRG5GC|Harsha Basavaraj>, *XD -* <@W8GN57XPH|Jing Wu>, *PMO -* <@U079GDD2EUR|Ben Irwin> <@U08LXR6M59C|David Montanez> <@U03AV5A2Z0X|Ranjith Madhavan> <@U02PS1BGW6M|Bhavya Mittur> <@W8F0RAYP2|Amruta Kulkarni>
*`Quickbooks`* 
*Fusion -* <@W8FQEE09K|Leah Wetzel (she/her)> <@U02M9N6KWF3|Saumya Pandey>, *RBAC -* <@W8FL4UM8S|Riti Arora>, <@U06GESYJGHX|Shubham Kumar Gupta>, <@U03NBFSNCGN|Hitesh Khatri>, *Privacy:* <@W8GG7V8HL|Mary Rook> <@W8FQEUJ8M|Chez Prakasam> <@W017CM8JXRQ|Rucha Chattur> <@U02G3TM94HL|Sibasish> <@U075V5HAKGR|Pushkar Joshi> <@U032Y7H8S9H|Preet Sarai> <@W8F0SEC8Y|Noel Eicher> <@U01DVL3UBGQ|Priya Prasad> <@W8FMA76H2|Nitin Kant> <@WR1G1C6QL|Praveen Ujjwal> <@U06551CL4KT|Anjana C Suresh> <@U05MAQQUPV2|Debarati Ray> <@U06LMMX76TH|Sujata Dwivedi> <@WMXLSJMCJ|Gulshakh Kaur>
*`VEP`*
<@W8GG6EEH4|Meet Mehta> <@U07GT9NQNDR|Sanjeev Kanajanavar> <@W8F0U68RE|Rohan Karthik Adgala> <@U02DCA5JMFA|Shubhashish Tiwari> <@WB294U4UQ|Sean Foley> <@U02KPG6G9PW|Gregory Lehman> <@W8GG704VC|Alissa Murphy - limited availability> <@U02TPHN09K7|Rachel Shelby> <@U041KFP78A0|Max Wolitzky> <@W8F0RJD0Q|Bharath Brahmakal>
*`Intuit`*
*Billing -* <@W8FQC7Q05|Kundan Burnwal> <@W8GG8BK0E|Neelam Singh (MSE)> <@W8FL3F4KC|Suresh Krishna D>, *Trust & Safety -* <@U03MCPYCVFZ|Hava Yellin> <@W011ARYD00P|Taly Shaiber> <@WFBQDKXMW|Ifat Friedlander> <@U04CSET8UFP|Idan Yohanan> <@WVABJ5LBH|Keren Simchon> <@U059N17HQLD|Anuradha Gudapati> <@U065CN6LETX|Mai Marikovsky> <@WDKKNS80G|Meitar Porat (He/Him/His)>, *Legal -* <@U02KENZHH6J|Robyn Taylor> <@U021B9371LY|Brittany Carr> <@WP3HNSL7L|Barbara Sondag> <@U035ZCH9U9X|Charles Jin> <@U07L9C5CG13|SooMin Ko> <@U02KMDFK6M9|Liza Schmitt>
*`Leadership`*
<@W8FHYGK19|Jack Tam> <@U08KK7S6LAZ|Diana Williams> <@W8FQBMAN9|Andrew Firstenberger> <@U02KJG17Q0M|Tanisha Barnett> <@U06K8UTTSJE|Jing Wang> <@W8FL345L2|Shivang Shah> <@U08FZT8NEFL|Vikas Dharia> <@W8FQBM3RB|Jay Schirmacher (m. 18588293494)> <@W8FL70XEE|Snezana Sahter> <@WCMQW566N|Derek Schwartz> <@U08UECD6USE|Suneet Nandwani> <@U07UET4959V|Gagan Singh> <@W8FL3BYTU|Candice Pham>

This massive effort across the company would have not been possible without y’all! :smiling_face_with_tear:

:themoreyouknow-3626: :thread: *Please check out the thread for videos and more info!*
Thread: 11 replies (latest: 2025-10-21 15:41:19 PDT)
Reactions: yay (60), violently-celebrating (39), rocket (45), celebrate (29), clapping-all (20), heart_sob (14), congrat (10), teamwork1 (11), shipitparrot (4), bananavegan (3), raised_hands (1), rocker (1)

---

=== Message from Jack Tam (W8FHYGK19) at 2025-10-21 08:38:17 PDT === 
Message TS: 1761061097.757559
Congratulations on this massive effort!!
Reactions: plusplusplus (4), arm-wrestle-high-handshake-business (1)



---

=== Message from Diana Williams (U08KK7S6LAZ) at 2025-10-21 09:47:05 PDT === 
Message TS: 1761065225.922069
Congratulations team. Excited to see us continuing to improve the experience for our customers.
Reactions: awesome (1), plus-pulse (4)



---

=== Message from Louis Pan (U095D83P9UN) at 2025-10-22 07:19:12 PDT === 
Message TS: 1761142752.917479
Figured a little late is better than never... but wanted to announce this launch and give props to the crew that made it happen!

:rocket:*Unique Discount Codes in Email Automations*
E-commerce marketers heavily rely on discounts to drive sales (63% of e-commerce users surveyed send discount codes in nearly every email). However, Mailchimp lacks a scalable, integrated way to generate, send, and report on unique discount offers, pushing our prospects and customers toward competitors who have been offering these types of features for years. By implementing an end-to-end experience for unique discount codes, Mailchimp will cover a key competitive parity gap and further enable our customers to grow their GMV. We’ve reached our first step in this incremental process by releasing unique codes in automation emails. This has been a huge multi-team and cross-functional effort that has been talked about for years so we’re excited to see this come to life.

*Impact & Metrics:* 
We have two early adopters (*<https://myroamate.com/|MyRoamAte>* and *<https://www.mcafeeinstitute.com/|McAfee Institute>*) that are sending real emails with unique discount codes to their customers. We’ve also reached out and connected with a 3rd customer who provided negative feedback to hear their concerns and identified ways to make our experience better.

*What’s Next*
We’re investing in unique discount codes in order to:
• Improve our competitive positioning amongst email marketing platforms
• Provide foundational discount code engine to activate discount codes across other surfaces 
• Allow us to win and retain higher-complexity Shopify customers that will help power MRR and AOV growth 
This initial launch of unique discount codes is a small first step towards our vision enabling a native unique discount code offering in Mailchimp, and provides the foundational infrastructure that unlocks our ability to extend unique discounts across additional surfaces in Q2.

It really took a village so wanted to do some shout outs :clap::trophy:
<@U07PQDS6F62|Josh Lynch> <@U08DYEMBSSG|Jason Cross> <@U02KJFNSB6H|Philip Allen> <@U085B0VAFHV|Nalin Ahuja> <@U08HFR40GP5|Olufisayo Oluwadiya> <@U031QMC5V32|Em Whitney> <@U03TANAE9AR|Spencer Reynoso> <@U093R5DQRG8|Nick Lancaster> <@U035CBMRTND|Nathan Leggatt> <@U06MWRJ6EQ4|Mary E Ellis> <@U02LB4SBY0Y|Paul Lee> <@U07NFKLFBKK|Akira Leeks> <@U02KJE9JALV|Michael Hawkins> <@U03R9TTF7FY|Abby Barnett> <@U02K6LY0X63|Jessie Brown> <@U02LB3PKAHW|Matt Castilla> <@U02KZV70EQZ|Jasmine Davis> <@U02KPGZ4HHS|Jane Guthrie> <@U02KJA0C137|Erin McCue> <@U03C0H8SPPX|Christian Vadi> <@U02KMBTRKL2|Jenna Fitzpatrick> <@U07Q8VAAMEV|Beka Rice> <@W0132PNAC9X|Devin Mercier (he/him)> <@U02KEJR5LP8|Jeremiah Edmond> <@U03V70QRTRQ|Mythili Gopikanth> <@U02KME26NUB|Michael Pazinets> <@U06K1M3KGHZ|Laura Guillen> <@U07PJK7TTPE|Brooke Addison> <@U02K6LEHGKZ|JB Lovell> <@U02KMCWL9LJ|Madeleine Stein> <@U04SYBP56JZ|Michelle Ducote> <@U02KJEHK677|Neil Desai> <@W8FHZJ4TV|Risa Shen> <@U02KJF76MU5|Rujuta Apte> <@U06QWR7FV9T|Elizabeth Bertasi> <@U02P9STSQGZ|Becca Walsh> <@U08J8FFFVAL|Stam Paterakis> <@U085DCH3MCN|Josh Bernhard> <@U02KEHAB5U6|Claudia Majors> <@U08T58BVD8R|Lindsey Dillon> <@U07J4NHVCBU|Kyle Johnson> <@U04D7TX5LDB|Ryan Hungate> <@U02KJ15KCA1|Brooke Hatfield (she/her)> <@U02Q1AFB12P|Nina Zhang> <@U02K6K3VC2K|Emily Roberson> <@U03DJNFKW4T|Nicole Robinson> <@U02K6PULZQX|Pooja Berrong>, <@U086MMX7W0M|Juliana Simoes> <@U079SMT5UTA|Matt Cimino>
Thread: 6 replies (latest: 2025-10-22 18:00:09 PDT)
Reactions: hooray (31), dancedoggo (20), discount (16), dance-bro (11), raised_hands (8), raised_hands::skin-tone-2 (2), tada (4), raised_hands::skin-tone-4 (1), money-bag (3), raised_hands::skin-tone-3 (1), excited-dog-558 (1)



---

=== Message from John Healy (U06FV7BTWTU) at 2025-10-22 09:42:59 PDT === 
Message TS: 1761151379.324489
:firework: *Reintroducing Mailchimp Transactional* :firework:
We’re excited to share that Mailchimp Transactional (formerly Mandrill), our platform for sending critical, event-driven communications, just got its biggest upgrade in nearly a decade. Building on a strong foundation of 35K paid users and $30M in annual revenue, these updates mark the start of a new era for Mailchimp Transactional, marked by deeper integration, product innovation and growth.

:rocket_launching: *What we launched:*
Transactional SMS is now GA, meaning customers can send time-sensitive messages like purchase confirmations and password resets via both *email and SMS* in all supported markets. The *new UI*, built on the Mailchimp Design System, delivers a modern, cohesive experience aligned with our core marketing platform, while *new API docs and an OpenAPI spec* make integration faster and more reliable for developers. The team has worked tirelessly to modernize the platform while preserving the rock-solid reliability our customers trust, including its 99.99% uptime and over 99% delivery rate. This marks a huge leap forward in the developer experience and sets the stage for future innovation.

:announcement-loud: *How we’re activating*
Today, we re-introduced Mailchimp’s Transactional offering to the developer audience, activating a multi-channel strategy to position Transactional as a fast, reliable solution to deliver critical, user-initiated messages across email and SMS. Key updates include:
1. <https://mailchimp.com/developer/blog/|Announcement post> and technical blog posts on<https://blogs.intuit.com/2025/10/22/reintroducing-mailchimp-transactional-for-your-email-and-sms-needs/| Intuit Developer Blog> , with supporting Exec LinkedIn posts from Jack T. and Eric A.
2. Optimized SEM strategy driving traffic to the <https://mailchimp.com/features/transactional-email/|updated landing page>
3. <https://docs.google.com/presentation/d/1g8HsN61XT1r2cNJfzdjMC03ROVSZkU60wq3NqLhgtD8/edit?slide=id.g38d3f1abdca_0_0#slide=id.g38d3f1abdca_0_0|Training> and <https://intuit.seismic.com/app#/doccenter/00852382-edc9-4813-8373-cf155aab7b0f/doc/%25252Fdd7a1b1e88-a432-5b72-de05-260fec22b35d%25252FdfMjQ3M2I0OTktMzMwNS00YTUzLWFlN2UtNDlmNWViMDFjMDcz%25252CPT0%25253D%25252CUGxheWJvb2sgLyBTZWxsZXIgR3VpZGU%25253D%25252Flf211f3a0e-1828-4631-890b-43242ec82a2c//?mode=view|enablement> inclusive of new claims, pitch deck, one-pager
4. <https://www.figma.com/design/tEEBEklU7ZF4P1FnBi2ZFO/Transactional-SMS-Launch?node-id=3312-429&p=f&t=4bXyMxhHD4keGgaN-0|Emails + IPDs> targeting existing Transactional and SMS users promoting Tx SMS
5. New <https://www.youtube.com/watch?v=tEWU6ST89qU|YouTube tutorial> on how to use Transactional SMS (going live on 10/22)
:question: *Why this matters:*
By introducing Transactional SMS, we’re enabling businesses and developers to reach their customers instantly, through the channel that best fits the moment. At the same time, aligning Transactional’s UI and developer experience with Mailchimp’s broader ecosystem makes the two platforms feel less standalone and cedes some of the exciting ways we plan to continue removing friction between marketing and transactional workflows.

:mag: *Early Signals*
We are already seeing early adoption with four customers actively sending Transactional SMS, including a new $40K MRR customer who has made more than 182K sends since signing on last week.

:thankyou1: *Special Shoutouts!*
• *Tx:* <@U02KJAK7GA1|James Moriarty> <@U02KZVD44TT|Jon Shogren> <@U02KPJ01EVA|Josh Campbell> <@U02L01LC801|Matthew Grove> <@U02KEGVE7UN|Christian Barnard> <@U02L0377N81|Patrick Murphy> <@U02KMAT1KT4|Grace Lane> <@U02VDDRRUG7|Stephen Tiedemann> <@U02KMBDS7AP|Heather Dartz> <@U04SQQF50DP|Kamrin Kennedy> <@U07S0EZPFST|Cristian Barbu> <@U03TDGMMFM1|dario_el-badry> <@U04739FF7M5|Adam Williams> <@U03TAMKCM37|Patricia Blackwelder> <@U02LB3HSDRN|Marissa Rivera> <@U02LB7537J4|Zac Wall> <@U02KJF76MU5|Rujuta Apte> <@U02L01PENRF|Mark Maynard> <@U02KEP40TL6|Sarah Segars>
• *SMS:* <@U03J3GGU5T3|Jeremey Nofzinger> <@U03NU55364D|Satish Sambandham> <@U07NM1TFPAB|Zach> <@W013E2DDP3J|Alina Rainsford> <@U03TDLSFYH0|Ben Marks> <@U06QHNDKYQK|Leo Lin> <@U02KJEHK677|Neil Desai> <@U076PQ83WPJ|Ana Bell> <@W8FQBKGUD|Dustin Yu> <@U02KEJR5LP8|Jeremiah Edmond> <@U07S4GH0JT1|Pascal Allen> <@U04UXHWUGHL|Ricky Amparo> <@U05GSV3QRHC|Daimen Williams>
• *GTM:* <@U04G5KNNVUM|Katie Witkowski> <@U02L01GJVC1|Mansi Gupta> <@U06P00YMHS7|Steve Lindberg> <@U06V0MUJNC9|Brooke Frazzetto> <@U04P04QEE6T|Ozi Opurum> <@U02RGGQ757U|Laura Adams> <@U05SSKAAMU7|Leo Oliveira> <@U02PHER72E6|Rai Robledo, MFA> <@U04DTC9ACLF|Brittany Reeves> 
• *Quality:* <@U02KPG6G9PW|Gregory Lehman> <@U02K6DM848P|Brendan Tucker>
• *Data Science:* <@U02KPJDJ3N0|Kavita Mani> <@U09AEP1PGSH|Adharsh Rajendran> <@U02KPMF42P6|Rachel Parks>
• *VOC:* <@U02KPJS0412|Kate Massengill> <@U02KEQFQ4DU|Travell Williams> <@U02L03X7BFB|Rachel Dagley> 
• *Support*: <@U02KP90J3K6|Ben Davis> <@U02KMCPM403|Katie (Bebop) Brennan> <@U084ZTZF15E|Faye Harris> <@U02M94SS0E8|Dozie Udezeh> <@U0335A7DJ0M|(TX) Josh Hammonds (Chance)> <@U03394Z26TV|(TX) Laettner Fulford> <@U03323HLEF8|(TX) Gabe Salvador (Jordan)> <@U02K6NQCG6B|Michael Martens>
• *HA:* <@U02KEED6LTG|Ankur Bag>
• *Legal:* <@U04FF36UREJ|Lina Lozano Oviedo>
• *Technical Content:* <@U02K6K3VC2K|Emily Roberson> 
• *Leadership:* <@U07AX5J7MFB|Eric Anderson> <@U02LB66UA1E|Shani Boston> <@U08KK7S6LAZ|Diana Williams> <@U054QGJRYJF|Adam Anger> 
Thread: 19 replies (latest: 2025-10-26 17:10:28 PDT)
Reactions: celebrate (60), nice2 (31), mandrill-sunrise (24), party-blob (23), lit (8), joe_lfg (6), amazing45 (5), mandrill-joy (8), party-cat-2 (6), blob_cat_sms_intensifies (5), thankyou1 (5)



---

=== Message from Diana Williams (U08KK7S6LAZ) at 2025-10-22 18:00:09 PDT === 
Message TS: 1761181209.095169
Yes! So excited for drop 1 of 2 to get out the door. Next up SMS! This is excellent!!
Reactions: yes3 (3)



---

=== Message from Anuradha Gudapati (U059N17HQLD) at 2025-10-27 15:24:30 PDT === 
Message TS: 1761603870.996829
Cross posting for visibility.
Reactions: rocket (4), wave (1), clapp (2), wave::skin-tone-5 (1)



---

=== Message from Chima Okechukwu (U03AME5740K) at 2025-10-28 07:39:09 PDT === 
Message TS: 1761662349.882549
_*#SHIP IT:*_ :green-light-siren::green-light-siren:

:rocket-launch::rocket-launch: *Reducing Friction in Fusion by pushing back the Plan Step for Non-purchase intent customer* :rocket-launch: :rocket-launch:

:emailintensifies:*Executive Summary*
While other work (<https://docs.google.com/document/d/1GjPNWBxLoiRWAT5Xr4Ka7wLyVX1su3cyhXwtdX73S7c/edit?tab=t.0#heading=h.d0vqclaw2qvx|link>) drives click through rate on Fusion Marketing app L0, we still have an opportunity to optimize the Fusion>MC onboarding flow to drive more customers into mailchimp.

The current completion rate in the Fusion>MC flow, although higher than the completion for organic  <http://Mailchimp.com|Mailchimp.com> acquisitions (78% vs 72%), isn’t optimized based on our learnings and isn’t leveraging the current best-in-class technologies we currently leverage on our default flow.

:jumpingstar: *What did we launch*
We pushed back the plan step for non-purchase intent customer onboarding to Mailchimp from QuickBooks.

Figma of the experience: <https://www.figma.com/design/pHgYZXavfnM2CRBBOq81Tf/MC-Fusion-Onboarding?node-id=215-110114&p=f&t=ms6JfvM89viBqFpc-0|link>

:shark_yay: *Analytics Insights:*
• Experiment results: <https://docs.google.com/presentation/d/1u1yrNNP8xIb5cyCwffEY3xZ27Fn2sj2HyRSPXr6c2WM/edit?slide=id.g39d8cb5e396_0_760#slide=id.g39d8cb5e396_0_760|link>
 
:celebrate: *Why this is big:*
• Opportunity to drive onboarding completion rate for customers onboarding
 
:hug:*What is next:*
• Follow up with additional data review to confirm if the results are maintained.
 
*Special Shout Out:*
:clapping-1772: _*This would not be possible without this amazing team:*_
• Product: <@U03AME5740K|Chima Okechukwu> <@U06QRS4SEBC|Rianna Schanno>
• Design: <@U02TP8JFQ4Q|Chris Keimig> <@U02104JK78A|Haemin Hwang> <@U03K5MLFBS4|Chris Sywassink>
• Eng: <@U0775UBDL3T|Vessy Shestorkina> <@U03C6DP87PF|Mostafa Derakhshan>  <@U060RFM8D27|Kranthi> <@U06K8UTTSJE|Jing Wang> <@W8GN4BUBH|Danh Dang> and <!subteam^S063NQFRQSU> 
• TPM: <@U02KZTXSPTK|Erica Jones> 
Thread: 5 replies (latest: 2025-10-28 10:14:42 PDT)
Reactions: rocket (11)
Files: EDD - Leveraging Creative Assistant to Drive MC Attach (ID: F09HAJV5UET, application/vnd.google-apps.document, 0 Bytes), Fusion NonPurchase Intent Experiment Pre-Post Readout (ID: F09PHQPTDPT, application/vnd.google-apps.presentation, 0 Bytes)



---

=== Message from Joshua Fischer (U07RNSH0256) at 2025-10-30 12:12:09 PDT === 
Message TS: 1761851529.731699
*TL;DR We saw 23% more people* (49.6% vs 40.4%) *and 37% more FTUs* (46% vs 33.5%) *resizing an image on Nuni by allowing customers to resize (or crop) directly from the canvas rather than only from the side panel. However, we did not see an impact on our primary metric of payoffs during the life of the test (*"Nuni Inline Image Editing and Cropping")

_Customer Problem_*:* I am a customer using Mailchimp’s Nuni email editor trying to change how the images look and are sized in my email draft But I cannot easily make them look the way I want Because The editor does not have the functionality or ease-of-use of other visual editing tools.

_What was launched?_ (see video attached):

  *Before*: Resize an image by going to the left rail, selecting the "scale" tab then moving the slider.  To crop, click 'edit image' which opens a 3rd party full screen pop-up
  *Now*: Resize an image by moving the block's corners directly on the canvas.  Or click 'crop image' and crop also directly on the canvas.

_What was the impact?_

We concluded our test once we dropped below the risk threshold, however at that point the impact on our primary metric of payoffs (people with 1+ send) was flat.

In terms of feature usage, however, we saw 23% more people resizing any images (49.6% vs 40.4%), +917 bps) - using either the old or new method - and 7% more taking any editing action (resizing, cropping or clicking the edit image button).

These numbers were even higher for FTUs not familiar with our editor, with 37% more (46% vs 33.5%, +1250 bps) new people successfully resizing an image vs the old UI control. *This means a lot more customers are figuring out how to take a fairly essential action in the email editor.*  And we have seen this usage of the new image editing features sustained since we rolled out to everyone.

_What's our Interpretation?_

The large increase in usage for this core feature - resizing images is one of the most commonly taken actions in Nuni - shows that even common tasks may not be clear in our current experience.  However, it also is worth noting that making this clear UX improvement that directly drove *demonstrably more usage did not directly translate into a sizable increase in topline metrics like sends or payoffs during the duration of the test. This is an important lesson as we look to both move topline metrics and improve our customer experience.*

Major praise to the team who spent a considerable effort making this a reality:
Design: <@U03QJC545C2|Ashley Wiesner> <@U02KJA0C137|Erin McCue>
Engineering:  <@U075AS34TME|Shawn Moore> <@U06RKUADWF3|Bryan Erazo> <@U0946BZ3QTW|Mike O'Dell><@U02K6LEHGKZ|JB Lovell> <@U06GTAA3E8G|Justin Little> <@U02KM7S28TU|Craig Rodrigues> <@U02KEK4H81L|Jackson Yoder> <@U0736NUC1PV|San'Quan Prioleau>
Data: <@U055LGZB276|Brian Fong><@U02QFTEHKB9|Kevin Martin>
TPM: <@U02K6LY0X63|Jessie Brown><@U02KJ5X1V3P|Cary Duncan>
Product: <@U07RNSH0256|Joshua Fischer>
<https://docs.google.com/document/d/1yzMmd0QM56JNw-2WYU2NvWJoZ1fUxUbYEytw1BaraRs/edit?tab=t.0|PRD>
Thread: 3 replies (latest: 2026-04-17 12:46:33 PDT)
Reactions: clapping-1772 (9), clapclap (7), blobross (3), freddance (5), rocket (7), rocket-party (3)
Files: new resize and crop hotness (1).mp4 (ID: F09QLS5TXH6, video/mp4, 19.4 MB)



---

=== Message from Frank Persico (U03KUBTCSG1) at 2025-11-03 09:02:04 PST === 
Message TS: 1762189324.913769
*#SHIP IT: Wix Bookings & Services Segmentation Condition*
*What We Launched* :rocket:
Hi all! I'm excited to share that as of today the Segmentation team has launched a new enhancement that allows users to target their campaigns based on their customers' booking activity in Wix. Thanks to the close partnership between the Audience & Segmentation team, the Integrations team, and the CDP team this release will unlock new marketing options for our professional services users that want to tailor their marketing to their new and existing customers.

*The Customer Problem* :slightly_frowning_face:
Following the <https://intuit-teams.slack.com/archives/C03TLJNADSP/p1757437311778949|recent launch> of the improved Wix integration that consumes booking and services data the roughly 70% of Wix users that are hybrid professional service-based businesses still had limited options for targeting their bulk Mailchimp campaigns. These users sent ~1.4B emails from Wix's native email tools in the first half of 2025, however few of those users would be likely to switch to Mailchimp as their primary marketing platform if their data wasn't usable here.

*The Solution* :blob_thumbs_up:
As of today all users in Standard and above plans have been given access to the new Booking Activity segmentation condition. Some examples of the segments users can now create include:
• Prior customers that had a booking within the last month but didn't make a follow up one afterwards
• Subscribers who booked a specific category of services (manicures, oil changes, hot yoga classes, etc.)
• Contacts that have booked individual classes but have yet to book a whole course as a package
This enables our users to send bulk messages that are tailored to each contact, creating more personalized marketing campaigns that drive better performance.

*What's Next* :next:
This is our first segmentation condition that uses non-ecommerce integration data and we're excited to keep expanding the options we give our users going forwards. In the future we'll be extending this condition to accommodate bookings from other integration partners like Calendly and Acuity to ensure we enable this capability for as many customers as possible.

:champagne: *Please join me in thanking the people that brought this launch to life!*:champagne:
*<@U04925BQ27M|Ade Ajanaku>* *<@U02KEGFKTPG|Cromwel Pestano>* *<@U05KZB08WRY|Jon Griffin>* *<@U07Q70L7BC5|Vova (Vladimir) Shechtman>* *<@U07A31AD7UZ|Thomas Grundy>* *<@U035AGFSBRC|Sabrina Harris>* *<@WPDQYNNA0|Amogh Mundhekar>* *<@U03R9TTF7FY|Abby Barnett>* *<@U02KJFNSB6H|Philip Allen>* *<@U07USKD0MA5|Shefali Dalal> as well as the CDP data engineering teams*
Thread: 3 replies (latest: 2025-11-06 19:38:20 PST)
Reactions: rocket (14), awesome (12), clapping-all (6), tada (5)
Files: Wix Gif.gif (ID: F09QCLF1PTP, image/gif, 877.2 KB)



---

=== Message from Diana Williams (U08KK7S6LAZ) at 2025-11-03 09:10:55 PST === 
Message TS: 1762189855.165899
Love the customer focus! Key use cases unlocked!
Reactions: rocket (1)



---

=== Message from Devin Mercier (he/him) (W0132PNAC9X) at 2025-11-06 06:00:23 PST === 
Message TS: 1762437623.921669
:send-it: *LAUNCHED: Send Time Optimization (STO) V2.1 delivers higher C2 engagement through smarter predictions* :clockeod:

:test_tube: *Overview:*
We’ve launched *Send Time Optimization (STO) V2.1*, an upgraded model that helps marketers send emails at the ideal moment for their audience. Building on the predictive foundation of V2, this release improves time localization and engagement prediction — helping C1s achieve better open rates and stronger adoption of recommended send times. The goal: more reliable, personalized timing to drive campaign performance and user trust.

:chart_with_upwards_trend_intensifies: *Impact & metrics:*
Running as an experiment the past couple of weeks, STO V2.1 has shown clear performance gains over V2.0:
• *+10.6% relative lift in open rate* compared to V2 (~2% absolute difference; 20.91% vs. 18.90%).
• *Recommendation adoption up +17.1% relative* (~7% absolute increase; 49.98% vs. 42.67%).
:upvote: *Why this matters for retention:*
Recent <https://docs.google.com/document/d/1GTnR0DszcaV78uHZBfPWghjj7_b21aBtiezwYTi0Xhw/edit?tab=t.0|churn analysis> shows that *open rate is one of the strongest behavioral predictors of customer retention*, independent of list size or tenure. Users with low open rates are *2.2× more likely to churn* than those with healthy engagement. In other words, when users’ campaigns get opened more often, they stick with Mailchimp longer. Features like STO that lift open rates directly strengthen our retention flywheel — by improving engagement, driving more successful sends, and reinforcing perceived product value among both new and tenured users.

*Gratitude/shout outs:*
Huge thanks to everyone who brought this to life: <@U07QE0U9MN0|Vaishali Singh> <@U06MY7FV9R7|Matt Mills> <@U076X3M3KB7|Mike Belov> <@U02KMB9T8GJ|Joshua Mackey> <@U02KPLAS31S|Mike Walker> <@U064FLW0QAK|Taylor Horton> <@U07B5L5983F|Cassandra Marshall> <@U055LGZB276|Brian Fong> <@U07RKQ1P8Q2|Yizhou Qiu> <@U02K6JTUE4X|Emily May Curtin><@W94L19RCJ|Joshua Ankele> <@U076X3M3KB7|Mike Belov>
Thread: 9 replies (latest: 2025-11-18 16:43:13 PST)
Reactions: ty_thankyou (6), yay-yay (9), mushroom_celebration (3), rocket (13), time_loop (2), nice-pink (3), wow3 (4)



---

=== Message from Louis Pan (U095D83P9UN) at 2025-11-06 14:58:35 PST === 
Message TS: 1762469915.003319
:rocket: *Unique Discount Codes in Email Automations - Fast Follow Enhancements*
Today, we launched enhancements to our Unique Discount Codes in Email Automations. These enhancements fixed cosmetic issues that we weren't able to get to before MVP launch and addresses important early customer feedback regarding the difficulty of testing unique discount codes end-to-end.

With this release we've:
• *Improving the preview experience:* Previews now show a “real” unique discount code so that C1s can more accurately see the final email that a C2 would receive. 
• *Enabling Test Sending:* C1s can now test the end-to-end experience of sending, receiving, and redeeming discount codes across Mailchimp and Shopify through the test send feature in the email builder without having to publish the journey. 
• *Streamlining the Merge-Tag:* The unique discount merge-tag is now more user-friendly, removing the need for a long ID string in the builder.
*What’s Next*
Although this is a relatively “small” improvement, it goes a long way to make sure we’re ensuring our  customers have a polished, full featured discount code offerings in Mailchimp as we work towards activating unique discount codes across more surfaces in SMS, Bulk campaigns and Forms in Q2.

*Shout outs* :clap::trophy:
<mailto:em_whitney@intuit.com|Em Whitney>,<mailto:spencer_reynoso@intuit.com|Spencer Reynoso>, <mailto:akira_leeks@intuit.com|Akira Leeks>, <mailto:michael_hawkins@intuit.com|Michael Hawkins>, <mailto:jenna_fitzpatrick@intuit.com|Jenna Fitzpatrick>, <@U08DYEMBSSG|Jason Cross> , <@U079SMT5UTA|Matt Cimino>, <@U086MMX7W0M|Juliana Simoes>
Thread: 2 replies (latest: 2025-12-03 10:39:53 PST)
Reactions: rocket (14), yay-yay (8), pretty (2)
Files: Screenshot 2025-11-06 at 5.55.48 PM.png (ID: F09RQSG17FB, image/png, 220.3 KB)



---

=== Message from Curt Shearer (U02KZSQSXAM) at 2025-11-17 09:29:43 PST === 
Message TS: 1763400583.254879
*What: In-Product Amended Terms of Use for New Customers* :co-sign: 

We’ve just launched a major enhancement to the sales *new customer acquisition* process that’s expected to *save* *150 person hours per month* and drive an *additional* *$50K in incremental MRR!*

Previously, negotiating defined discount terms was a time-consuming process requiring external documents, multiple approvals, and an average turnaround time of 2 days to finalize deals.

With this new update, prospects can now seamlessly agree to defined discount terms directly within the checkout flow—no extra documents, no manual approvals! *This revolutionizes the close process, cutting it down from days to mere minutes.* A seller and prospect can agree on a deal, and within just 5 minutes, the prospect will have their new account up and running, subscription activated.

Huge shoutout to these individuals for making this happen :thankyou1: <@U02LB1FTC9W|Joe Stevens> <@U03A50JQBA9|Shasikala Papisetty> <@U04F7GC809E|Poornima Padubandla> <@U080J17B61E|Prakash Bhatnagar> <@U07GQ2T6L7R|Sudhakar Panjala> <@U07PV9VL1HD|Omar Carrasco> <@U02L04VGWEM|Stacia Lorenze> <@U02KMFNH082|Scott Cleveland> <@U032GEW7U0Y|Brent Hallinger> <@U079C88A62Y|Colin James> <@U06SKLW6U1K|Tom Eschbacher> <@U02KEMCGLVC|Michelle (Meesh) Whitley> <@U03TYGJA7D2|Nick Smith>  <@U05QNVD0KHP|Cuc Le> <@W8FMB5WKW|Barb Magner> <@U02K6NH28B1|Lewis Beard>
Thread: 4 replies (latest: 2025-11-17 11:15:07 PST)
Reactions: raised_hands::skin-tone-3 (6), raised_hands (18), raised_hands::skin-tone-2 (3), raised_hands::skin-tone-5 (1), raised_hands::skin-tone-4 (3), rocket (6), awesome (1)



---

=== Message from Taylor Mattson (U05AMM7NF5J) at 2025-12-05 08:16:22 PST === 
Message TS: 1764951382.495089
:rocket:*Reporting & Analytics launches the Bot Filter for Email Opens + Clicks and SMS Clicks* :bot2:
For years customers trust in Mailchimp engagement metrics has been decreasing due to the presence of non-human activity in open and click metrics. Non-human activity can come from a number of places like web crawlers, corporate firewalls, inbox provider security, and mobile device OS. These "bots" pre-open and pre-click both email and SMS messages which register as clicks and opens in our database. Analysis done earlier this year estimates that ~38% of email clicks are as a result of bots and ~72% of SMS clicks are as a result of bots (analysis on all clicks in our DB for 30 days).

Today we are delivering a customer-first solution that finally closes the years-long gap in the industry by eliminating bot contamination and Apple MPP blind spots across email and SMS. Our approach provides deterministic, third-party–validated detection and gives customers trustworthy, transparent, and customizable reporting that reflects real engagement.

:sad-customer: *Customer problem:*
*I AM* a small or mid-size business
*I AM TRYING TO* make evidence-based marketing decisions to improve conversions
*BUT* I cannot trust open and click metrics in Mailchimp reports
*BECAUSE* my metrics are inflated due to bot activity — something I see clearly when Mailchimp’s numbers don’t align with Google Analytics or when reports show multiple opens/clicks occurring immediately after sending, making my tests and optimizations unreliable
*WHICH MAKES ME FEEL* frustrated and distrustful of the platform’s analytics

:chart_with_upwards_trend_intensifies: *What was launched?*
This experiment is exposing *all customers*  to the new Bot Filter, which includes:
• *Bot Detection Service:* A new service that classifies clicks as bot or human prior to reporting. Unlike competitors who rely primarily on heuristic behavior patterns, our system uses deterministic signals such as user agent signatures, blacklisted IPs, and threat intelligence groups. This increases confidence in bot detection and reduces false positives.
• *Global Bot Filter Settings*: Customers are able to customize which metrics bots are filtered with support for email opens, email clicks, and SMS clicks
• *Bot Filter Indicator*: On supported experiences, an in-context filter on/off indicator is introduced with a 1-click link to bot settings to easily adjust if needed.
    ◦ *On the following pages*: Email report, Custom Reports, SMS Report, Homepage, Marketing Dashboard
    ◦ Coming soon: All campaigns (~1 week), Click Map/Click Performance (after the holiday), Automations Flow Report (when modernized)
:transparent-value: *From -> To*
Inflated Click Metrics → More realistic click metrics email and SMS without known bot contamination
Apple MPP Filter on _*some*_ pages → Global, set it and forget it Apple MPP filter that touches more surface areas
No clear insight into open and click metrics →  Peace of mind that metrics are a true depiction of human activity

:experiment: *How will we define success?*
• Reduction in VOC feedback related to data quality/bots
    ◦ Baseline: 37%
    ◦ Target: Reduce by 70% to ~10.5%
• Reduction in % of email clicks that are bots in reporting
    ◦ Baseline: 37%
    ◦ Target: Reduce by 20% to ~29.6%
• Reduction in % of SMS clicks that are bots in reporting
    ◦ Baseline: 71%
    ◦ Target: Reduce by 50% to ~35.5%
:next: *What’s next?*
This launch is an A/B test and we expect to deliver some early results next week. In the meantime, we will monitor VOC channels and continue to hop on any issues that arise (so far we've seen just 1 since we started rolling out on 11/24 which was minor and has been fixed). As R&A continues to modernize remaining experiences like All Campaigns metrics, Automations Flow Metrics, click performance, and click map. the bot filter will roll out to these experiences in parallel. The next phase of the project will include adding support in our bot detection service for Google's public proxy IP list.

_Early Success Story_
This week we've already been able to give an at risk customer the feature early in order to save their business and better meet their needs (shoutout to <@U06RWLB4Y75|Chelsea Cartwright>). We will continue to work closely with this customer and make sure we address any feedback.

:reportingsquad: *Shout outs & HUGE THANKS*
_This project took a huge effort from so many cross-functional teammates. I truly could not have done this without so much support from leaders, and everyone's commitment to making our customers' experience so much better. I also want to shout out the CSM/Sales/L&D teams for their commitment to learning and understanding the feature early so they can better support our customers!_

Product: <@U05AMM7NF5J|Taylor Mattson>
Design: <@U02L04W0FPT|Tamlin Tromp>
Engineering: <@U0580HUFQ00|Scott Adams> <@U046WDQCP0R|Cavin Myers> <@U03ALF0U1GR|Carson Britt> <@U02LB1Z7EU8|Justian Meyer>
PMM: <@U03HRFYTYUB|Simone Kovacs>
Data Science: <@U07ED705DHS|Aastha Sehgal> <@U0970UUFN80|Ashish Prakash>
Trust + Safety PD and Policy Teams: <@U025WABEPSP|Alejandra Solano> <@WFBQDKXMW|Ifat Friedlander> <@U07DJBS5XJS|Sailesh Vankadara> <@U059N17HQLD|Anuradha Gudapati>
Leads: <@W8FL6URHQ|Deepak Prabhakaran> <@U02KMG1BGBV|Shane King Zackery (they/them)> <@W8Z8R7STE|Nir Harel> <@U02KJENBBDK|Neveen Moghazy> <@W8FHXCZSP|Saikat Mukherjee>
Special thanks: CDP Engineering team, <@U02KEQP5A6S|Wei Jia> <@WP0ENL12Q|Deepak Mirani> <@U02KM9EKNFM|Chris McGee> <@U02KENZHH6J|Robyn Taylor> <@U040F42EC69|Haley Dutton> <@U02KMA9URKL|Evan Burke>

Experience Walkthrough <https://www.loom.com/share/3659d440c50c422a9d9d528a99642068?sid=ea222f9f-55d1-4bf1-a6f3-1b01f1f1a21b|Video>
Thread: 14 replies (latest: 2025-12-09 12:26:31 PST)
Reactions: yes3 (32), yay-frog (27), awesome_dance-3092 (13), clapping-all (21), lets_go2 (8), 100 (3), fire-ball (2), celebrate (1), bot2 (1)



---

=== Message from Rachel Shelby (U02TPHN09K7) at 2025-12-12 13:03:08 PST === 
Message TS: 1765573388.617169
:rocket: *VEP & GBSG CX Launched:  Unified Customer Health Score - Empowering Mailchimp Customer Success Experts to Stop Churn Before It Starts*

*Milestone Unlocked:* MC CS is the first team to unlock the Customer Health Score within the Account Health Tab in CXM, paired with Gainsight, we are setting a new standard for proactive, data-driven customer success.

:summary_icon: *Executive Summary*

We are shifting from reactive saves to proactive account management. With the launch of the Customer Health Score, Sales and CS teams now have a shared, early-warning radar for churn risk. By translating customer behavior into a “vital signs” grade, we are empowering experts to identify at-risk customers months before a cancellation request comes in, allowing for timely, high-value interventions that secure our book of business.

*What did we launch?*
• *A Precision “Vital Signs” Grade (1-5):* We now generate a weekly health score based on a weighted blend of four core outcomes.
    ◦ _Note on Scope:_ Right now, we are mostly checking their health based on our Marketing tools, but later on, we will start checking how they use our Messaging and Transactional products.
        ▪︎ Audience Growth (30%)
        ▪︎ *Deliverability (*30%*)*
        ▪︎ *Engagement (*30%*)*
        ▪︎ *Revenue (*10%*)*
• *The 90-Day Warning System:* The model compares current performance against a customer’s 90-day history, helping experts spot usage declines long before the customer voices dissatisfaction.
• *Smart Scoring Logic:* The model is dynamic. If a customer lacks sufficient data for a specific component (e.g., not enough periods for Audience Growth), the model automatically ignores that weight and re-normalizes the score based on the available data, rounding to the nearest whole number.
• *Traffic Light Risk Indicators:*
• 
    ◦ :red_siren: *Red (Score 1-2):* _Immediate Action Required._ Recent data confirms that churners consistently fall into this range.
    ◦  :yellow-alert: *Yellow (Score 3-4):* _Monitor & Nurture, Action Required._ Customers are stable but leaving value on the table.
    ◦  :green1:*Green (Score 5):* _Secure._ Star customers maximizing the platform.
• *Unified Visibility:* Whether you are in CXM (Salesforce) or Gainsight, the data is identical and updates weekly. Sales can see risk before an upsell call, and CS has a consistent data cadence to guide their weekly planning.
• *Automated Defense (CTAs & Playbooks):* We have operationalized these scores to drive immediate action. A drop to Yellow or Red instantly triggers a targeted CTA and playbook. This guides Account Managers through a 30-day health sprint, including:
    ◦ Performing deep-dive account health reviews.
    ◦ Sending templated, personalized outreach to re-engage the customer.
    ◦ Executing structured follow-up checks to ensure the risk is resolved.
*Measuring Success*
We are driving a fundamental shift in how we manage risk, targeting these material outcomes:
• :save: *High-Risk Save Rate:* Increasing the save rate for managed accounts from 37% to 40% (projected ~$1.2MM in annual saved MRR).
•  :clipboard: *Proactive Intervention:* Moving from ~150 to 200 managed risk cases per month, driven by consistency in how we identify struggling customers.
• :moneybag: *Revenue Protection:* Growing average monthly saved MRR from $640K to $735K.
•  :chart_with_upwards_trend_intensifies:*Customer Health (Team Goal):* Lifting the overall health of our book from 81% to 85%.
:crystal_ball: *What’s Next?*
• *Zero-Touch Risk Case Creation:* We are removing the administrative hurdle to fighting churn. Soon, a drop to Red will not just flag a risk, it will instantly operationalize it by automatically creating a formal Risk Case for experts. This ensures zero lag time between detection and action, letting you focus 100% of your energy on the save.
:celebrate-1632: *Thank You & Credits*
*This launch was a successful cross-functional effort!*
• *ICS Data Science & StratOps:* Your work established a strong foundation for proactively managing customer books, including robust models for generating insights and Tableau dashboards for assessing historical customer cohort trends.
• *MC DE and VEPCS PD:* This partnership keeps getting better and better! A huge shoutout for your agility and collaboration. Due to unforeseen circumstances, these teams successfully pivoted from our initial data pattern _without_ missing our go-live date!
• *Gainsight Team:* Thank you for building an AMAZING first iteration of the Customer Health Score Scorecard, CTA’s, and Dashboards in Gainsight!
*GBSG CX PM E2E Driver:* <@U02TPHN09K7|Rachel Shelby>
*GS BSA:* <@U02KPKHHZHS|Lily Killingsworth> <@U02KZUTQZQR|Heather Bryant>
*VEP PD:* <@W8F0RJD0Q|Bharath Brahmakal> <@U03SW565D18|Kunal Dixit> <@U09CBSE2B52|Sarang Borlepwar> <@U07GL9DURHA|Aniket Agrawal> <@U022XEW8XST|Nikita Bankar>
*MC DE:* <@U05A4D12BT8|Alexandra Pappas> <@U04QT5HV4AE|Xiao Han> <@U05B8V54DC0|Rich Archer>
*ICS DS:* <@U04J0JBPWP2|Sanjay Motwani> <@W8FHWDUUB|Wendy Anderson>
*MC CS:* <@U0988NX1J7K|Camilla Calhoun> <@U02LB089DHN|Danielle Lucas> <@U08FL1BSLNM|Cassie Henning>
*MC Enablement: MC Enablement:* <@U06L11GPRDH|Kasey Wilson> <@U04HA5T61A6|Zoey Brown>
*MC CS Strategy Ops:* <@U02KM81JD50|Andrew Barrocas> <@U0664FD1LTZ|Rohan Thakur>
*Leadership Team:* <@U03KWGUK8D6|Julie Zimmerman> <@U02K6NWDM7H|Marlene Mayfield> <@W8FL2QMQS|Anant Saxena> <@U07Q6JN5N6Q|Steve Sanchez>

*Resources:* <https://docs.google.com/document/d/14c5uHqC3EpQOrC8ByXqFf9R7F157QpRozbTUkn89ivw/edit?usp=sharing|MC Customer Health Score (CHS) - Release Notes>
Reactions: celebrate-3409 (22), tada (16), fire (13), yes3 (4)



---

=== Message from Devin Mercier (he/him) (W0132PNAC9X) at 2025-12-16 08:38:53 PST === 
Message TS: 1765903133.658189
:rocket: *Launched: Subject Line A/B Testing in Email Checklist*

Marketers have long found it difficult to optimize subject lines due to the rigid nature of the legacy A/B testing workflow, which was separated from the main email creation process. This friction led to inefficiencies and low adoption rates for subject line testing. We hypothesized that moving subject line A/B testing directly into the existing bulk email checklist would reduce friction and drive higher adoption. The results from our experiment were a *significant success*, showing a clear lift in both feature adoption and our primary metric and *we've rolled out to 100% of customers as of 12/5*.

:thonk: *Customer Problem:*
I *AM* a marketer trying to optimize my emails for better engagement.
*I AM TRYING TO* test different subject lines to see what resonates with my audience.
*BUT* the current A/B testing workflow is time-consuming and separated from my main email setup flow.
*BECAUSE* I have to navigate away from the checklist to create a test, which breaks my momentum.
*WHICH MAKES ME FEEL* frustrated that optimizing my emails is too difficult, so I often skip it entirely.

:test_tube: *What was tested?* We introduced subject line A/B testing directly within the existing bulk email checklist. This change added an intuitive access point allowing users to select up to 2 subject line variations and define settings directly in the workflow.

:chart_with_upwards_trend_intensifies: *Key Results & Metrics:* The variant proved to be stable (0.00 risk) and highly effective.
• *Primary Metric (Open Rate):* The variant achieved a *19.94% C2 Email Open Rate* (vs 19.35% control), an absolute lift of *0.59%*.
• *A/B Test Send Rate:* Increased by *~3X* (0.76% variant vs 0.24% control).
• *A/B Test Creation Rate:* Increased by *~2X* (1.14% variant vs 0.49% control).
• *Efficiency:* Create-to-Send efficiency improved significantly from *40% to 51%*.
• *Financial Impact:* Estimated effect size of *~$325K* in retained revenue:money_blob: 
:next: *What’s next?* Given the positive impact on open rates, the substantial increase in feature usage, and zero harm to guardrail metrics, we have moved to *100% Rollout* (completed as of Dec 5, 2025). We will now focus on monitoring long-term adoption and further optimizing the checklist experience to accommodate additional A/B testing in Q3.

:megaphoner-1707: *Shout outs & HUGE THANKS*
Product: <@W0132PNAC9X|Devin Mercier (he/him)>
Design: <@U04RXGCEPCY|Tracie Kreiss>
Engineering: <@U06T2RV5ALX|Anil Prabhala> <@U02KM9C1V3L|Dalyn Small> <@U02KJB6KQ9K|James Howard> <@U02KPGQGSVA|Jason Calhoun> <@U094059CKSQ|Jona Reyes> <@U077N1MCR6E|Bharathi Raja Palaniswamy>
Data Science: <@U07RKQ1P8Q2|Yizhou Qiu>
Leads: <@U06QRS4SEBC|Rianna Schanno> <@U09B1S1DZ6Y|Sundeep Nadendla> <@U02KMBDS7AP|Heather Dartz> <@U02KZMX4E6M|Celeste Mora (they/them)> <@U07AX5J7MFB|Eric Anderson>
Consults with the Growth Team: <@U08D0C42PJM|Andrew Spitz> <@W011K0R03SA|Arya Iranmehr>
Thread: 3 replies (latest: 2025-12-16 10:58:00 PST)
Reactions: happy_dance (32), awesome (19), rocket-launch (5), white_check_mark (2), rocket (8), celebrate (5), raised_hands (6), raised_hands::skin-tone-2 (3), raised_hands::skin-tone-3 (1), clapping-all (4), ab (2)



---

=== Message from Diana Williams (U08KK7S6LAZ) at 2025-12-16 12:41:10 PST === 
Message TS: 1765917670.587829
So glad we are getting this out to more customers. It's so valuable. Please work with Marketing to get all the claims we need and value proof-points to drive smart targeted adoption!



---

=== Message from Stephen Yu (U040C49798T) at 2025-12-18 12:31:55 PST === 
Message TS: 1766089915.729689
:rocket_launching: *Reporting & Analytics AI Agent (Project Alfred) - Alpha Launch* :blob-robot:
Today, businesses are heavily time-constrained and often lack marketing expertise to effectively maximize their marketing performance. They spend hours manually analyzing performance, with 53% of SMBs immediately investigating unusual performance and 38% dedicating weekly time to analyzing campaigns. Customers are looking for faster and proactive insights beyond the static reports that are pre-defined in Mailchimp today. *To address this need, we are launching an analytics agent that acts as an AI-powered analytics expert by your side natively within Mailchimp that transforms fragmented marketing data into insights and data-backed recommendations.  Through this change, we will evolve from passive reporting into proactive intelligence to inform next steps. This is an Alpha version to a small audience cohort starting with 100 Ecommerce users in Dec. and scaling to Beta beyond that.* Our goal is to provide clear and actionable insights that are easily accessible to customers, leading to higher user confidence in growing their business.

:customerproblem: *Customer problem:*
*I am* a business owner/marketer who is responsible for marketing operations
*I am trying to* grow my business by maximizing my marketing performance
*But* I am struggling to understand how my marketing efforts are performing and what I should be doing next
*Because* I am spending a lot of time in Mailchimp to conduct manual data analysis chasing dead ends and to figure out next steps
*Which makes me feel* like I am investing my limited time and effort in the wrong places to grow my business

:rocket4:*What was launched?*
We are launching an AI agent that is tailored for marketing performance analysis and optimization:
• *Marketing analytics through conversational experience:* Users can ask any questions about their Mailchimp data and see data-backed insights with transparency into how it is calculated
• *Dynamic analysis:* The agent is capable of dynamically querying, analyzing and synthesizing marketing insights, even for analytics that do not exist in the product today (i.e. Cohort analysis, product level performance, detailed conversion insights etc.)
• *Personalized responses based on user context:* The agent is context aware with personalized responses based on the user's marketing data, historical benchmarks, and supplemented with Mailchimp's knowledge base. The starter prompts and responses are research-backed and tailored based on the workflow starting with one of Mailchimp's strategic audience, Ecommerce users
• *Actionable next steps:* We will show users not just what happened but also what to do next by surfacing data-backed recommendations that are tailored to Mailchimp
:customer-obsession-vas:*Early customer feedback*
We are seeing positive customer VOCs based on user testing in their own accounts:
• _'Overall summary, it looks great, all the metrics that I would look at are there...'_
• _'I would definitely use this product instead, since it is native in the platform. I think it's super helpful...'_
• _'All that information is easy to read, I love it, I love it...'_
:chart_with_upwards_trend: *What are we tracking for success*
• *Insight to action:* Drive increase in meaningful actions completed from users engaging with agent
• *Adoption:* First time adoption, Repeat adoption
• *Eval - Relevance, Coverage, Accuracy*
    ◦ Current Baseline: 75% eval using LLM-as-a-judge supplemented with manual eval against user data
    ◦ Target: 85%+ eval as we scale to broader audience
• *Operational:* Latency, Error rates
:next: *What’s next?*
Our goal is to become the marketing intelligence layer that drives actionable insights. We have a robust plan to continue to enhance this capability and scale it to a broader audience into Beta & GA with key priorities focusing on:
• Enhance underlying data platform to ensure AI readiness such as ability to query dynamically in real time, broad data coverage and latency performance
• Iterate on E2E experience with immersive + assistive mode and data visualization 
• Continue to improve eval score and refine response output around insights, recommendations and system guardrails
• Proactively surface AI-powered insights contextually across common workflows
• Ability to complete actions on the user's behalf such as campaign management with agent to agent collaboration
:megaphoner-1707: *Shout outs & HUGE THANKS*
This was a cross-functional initiative involving many teams and I want to give a HUGE THANK YOU to everyone involved. This was a stretch project in Q2 and the team was able to come together to quickly deliver a transformative experience that reimagines how users analyze and optimize their marketing performance!

Engineering: <@U01J5GVP5GV|Kuntal Naphade> <@U09Q9KFSP8W|Jason Dudley> <@W8FMAA7S8|Yi Zhang> <@U08ALKME0VA|Inder>
AI Science: <@U02KM30QU10|Ben Leathers> <@U0793KXBF51|Bryan Smith>
Product: <@U040C49798T|Stephen Yu>
Design: <@U02L04W0FPT|Tamlin Tromp>
TPM: <@WP0ENL12Q|Deepak Mirani>
Data Science: <@U07ED705DHS|Aastha Sehgal>
Product Marketing: <@U03HRFYTYUB|Simone Kovacs>
Leads: <@W8FHXCZSP|Saikat Mukherjee> <@U08ALKME0VA|Inder> <@U064FLW0QAK|Taylor Horton> <@W8FL6URHQ|Deepak Prabhakaran> <@W8Z8R7STE|Nir Harel> <@U0970UUFN80|Ashish Prakash>

<https://www.figma.com/design/wfGlMExf1rxooLDPwh98dd/Marketing-analytics-agent?node-id=891-43842&p=f&t=t8xH6mDQc0j7DkpL-0|Design>
Thread: 14 replies (latest: 2026-01-30 16:12:35 PST)
Reactions: awesome (22), rocket (24), ai-intensifies (15), party-blob (8), mc (7), peanutbutterjellytime (3), yay (2)
Files: Analytics agent recording (Test account).mov (ID: F0A4W4FAZG9, video/quicktime, 53.0 MB)



---

=== Message from Jacquelyn Horgan (U02KMAN6V1R) at 2025-12-22 08:00:14 PST === 
Message TS: 1766419214.888739
:rocket: *EXPERIMENT: NEW PHONE COMPONENT ON CHECKOUT* 

*Launch date:* December 15
*Status:* Still running :loading:

:test_tube: *Overview:* 
As part of Tax Compliance, we're now validating a customer's location based on where they're using the Mailchimp product, using a variety of data points. One of the data points used is phone_number_country, which is a new data point we're collecting as part of the User contact information. Of those customers failing assessment, 50% of them have a previously saved phone number, but no phone_number_country. In order to increase adoption of this field, we're adding phone number to checkout, as part of the Contact Information section. We're testing two variants, one where the phone number is surfaced but optional, and surfaced but required to checkout. In either state, the phone component is only seen if the customer chooses to edit their Contact Information on Checkout.

:question:*Primary Question:* Can we increase phone component adoption for existing base without causing harm to checkout?

:chart_with_upwards_trend: *Early impact & Metrics:* 
• Objective 1, Do no harm: 
    ◦ Checkout rate is table across the control and variants at 24%, and we're surprisingly seeing a *3-4%* *improvement to purchase attempt success rate in variants over the control.*
• Objective 2, increase `phone_number_country` data: 
    ◦ Optional Variant and Control Variant are driving a *10% and 11% increase - respectively - of `phone_number_country` saved over control.* 
:koolaid-walk:  *Next Steps:* Continue to monitor experiment over recharge, and determine winner on January 5.
:clapping-all:  *Big thanks to*:  <@U0670DW10HY|Vrushali Ghodekar> for the dev work, <@U02KMFA7R2N|Ryan Simpson> for the testing, <@U02K6N931JB|Mac Dillard> for all the guidance on "How to run an experiment" (this is my first one!) and <@U045KSM7L8L|Mathew Deeb> for AI innovation so I could self-serve my own analytics for this experiment.
Reactions: rocket (7), woo-hoo (6), party-phone (2)



---

=== Message from Jacquelyn Horgan (U02KMAN6V1R) at 2025-12-22 13:43:05 PST === 
Message TS: 1766439785.640729
:rocket: *REVAMPED ANNUAL PLANS TO DRIVE ADOPTION FOR MANAGED CHANNELS*

*Release date:* December 18
*Business Problem:* Acquiring, retaining, and growing mid-market customers is a key part of our FY26+ strategy; however, our billing solutions are uncompetitive compared to peers and create a less than ideal experience for these larger, more sophisticated customers. Our primary solution to address the needs of these larger customers has been annual plans. However, since launch in February 2025, we have struggled to gain adoption primarily due to rigid discounting structure and misaligned seller incentives

*What was launched?*
• New Annual Plan list price at 5% implicit savings compared to Monthly plan. 
• Ability to discount further, as needed
• New sales incentives plan for Annual Plans
*What does it unlock?*
• Lead with the Annual Plan for New to the Franchise (NTTF) customers
• Reduce early-life churn by securing long-term commitment and driving initial product adoption 
• Ability to target at-risk mid-market customers who want stability in their billing, but don't necessarily need/want a discount. 
:chart_with_upwards_trend: *Early impact & Metrics:*
• Within 24 hours of launch, we booked 2 prospects to an Annual Plan via the Sales Offer Tool.
*What’s next?* The goal is to bring the annual plan to general availability. We're brainstorming :brainstorm-4737: and will begin testung into the best way to position the annual plan to existing and prospective customers.

:clapping-all:  *Big thanks to*: <@U032GEW7U0Y|Brent Hallinger> <@U02KEAE3DL6|Bryce Hammond> <@U045QK7AM1A|Anesia Smith> <@U02KZSQSXAM|Curt Shearer>  <@U07MYEG53JB|Rhomaro Tesfai-Powell> <@U02KEHPFLDU|Elizabeth Cason>, <@U02L00GFMEV|Koleen Henson> <@W8FMB5WKW|Barb Magner> <@U05QNVD0KHP|Cuc Le> <@U02TNUQ1868|Srinivas Manepalli> <@U047HMUGE82|Erin Szarpa> <@U02PWSQQ8A0|Emily McAnnally> <@U0988NX1J7K|Camilla Calhoun> <@U02KMFNH082|Scott Cleveland> <@U0372M44CMS|Andres Berdugo>
Thread: 1 replies (latest: 2026-01-05 16:22:15 PST)
Reactions: yellow_heart (13), yes3 (1), raised_hands (4), rocket (2), raised_hands::skin-tone-3 (1)



---

=== Message from Kim Gurvitz (U02CJJ8MM6G) at 2026-01-06 07:09:50 PST === 
Message TS: 1767712190.579199
:rocket: :gednovfy26-emoji-02: *Launched GED : Deja Review!*

:sirens: *Problem:*
The current process sends content for review every time it violates a policy, even if it has been reviewed previously. This redundancy burdens our reviewers and leads to inconsistent labeling, as different agents may tag the same content differently. These inconsistencies negatively impact our model training, increase leakage rates, and degrade the user experience, as a single user may receive varying responses for identical content submissions.

:merrgreen_exclamation_mark_:*Solution:*
Content that has been previously reviewed will now bypass the review process. Instead, it will be automatically labeled with the most recent tag it received.

:lightbulb:*What did we do?:*
• Updated our existing content hashing for more accuracy
• Created a new flow where if a campaign was already reviewed, we won't review it again and it will get the same label (pass/content violation) as the previous campaign.
• Review is "moderated" automatically - no need for human intervention and we don't lose any documentation.
:fire-orange-1: Why does it matter?
• This is *enhancing labeling consistency* as the the content is not reviewed by different agents anymore
• *Reduced EC reviews by 8%* from total volume
• Improved *customer experience* by being more consistent with our moderation
  :nextsteps: *Next Steps:*
• Using URLyzer to overcome dynamic links that changes the hash but not the content
• Fuzzier match: expand this idea to similar texts
 :clapping-1772: *Who made this possible:*
T&S Policy: <@U02CJJ8MM6G|Kim Gurvitz>
T&S PD: <@U07DJBS5XJS|Sailesh Vankadara>
T&S Analytics: <@WGKKK76BW|Dayna Kesten>
A2D: <@U086L06N38Q|Alazar Kessela>
T&S investigations: <@U0846SA67JL|Danie Haden>
Leadership: <@WFBQDKXMW|Ifat Friedlander> <@U059N17HQLD|Anuradha Gudapati> <@U04PRABR1GX|Tomer Shklar> <@W8Z9YUUE5|Noah Eyal Altman>
cc: <@U08EWUEJZNC|Sarit Ashtar>
Reactions: ball-awesome (5), trophy (7)



---

=== Message from Chima Okechukwu (U03AME5740K) at 2026-01-12 13:31:35 PST === 
Message TS: 1768253495.621299
:rocket-intensifies:*Drive MC Attach in Fusion - Marketing Hub Landing Page with Templates*

*Business Problem* 
A review of early Fusion data shows that Mailchimp’s 90D attach rate is 0.73% for both NTTF and QuickBooks users (lowest among ecosystem apps)2. The largest drop-off for Mailchimp Attach experience in Fusion occurs at the top of the funnel when a C1 clicks the Marketing app L0 (~0.6% conversion rate3). Thus, we see a huge opportunity to drive attach rate for QBks customers.

:ponyta-shiny:*What was launched?*

*From:* Static pricing-led landing page (see below)
*To:* Landing page highlighting our Done-for-you email templates (see below)

*Context*
• We know from prior research that customers want to explore the application before making a purchase decision. 
•  Additionally, we know customers resonate best with messaging around “saving time” as the reason to adopt Mailchimp
• Thus, we have a high conviction that if we promote our Done-for-you experiences, we will be able to drive MC attach because customers will realize the value of Mailchimp. 
• We launched a landing page highlighting the ready-to-use templates, so customers can preview and explore our Done-for-you experiences before they add Mailchimp. 
*Figma*: <https://www.figma.com/design/GAkusKgq76AdHxuW4GBPo9/Template-first-landing-page?node-id=15-23520&t=diTUtoRZtPEY6r9W-0|Template-first landing page>

:questionblock: *What does it unlock?*
• For our customers, it allows them to explore Mailchimp before they purchase or explore Mailchimp deeper.
• Big opportunity to drive attach rate by driving Sign Ups
:data-intensifies: *Early impact & Metrics*
• Seeing increased engagement we see on the QB marketing page, and this did translate into *>2x the number of MC signups*
    ◦ From ~150 Signups starts a week to more than 300 signup starts 
• Net new sign ups dropped off in the new user MC flow, resulting in more of a neutral outcome in terms of MC sign ups.
*What’s next?* 
• Iterate to address the drop-off post Sign-Up 
• Continually monitor the metrics for 90D values
  *Shout outs and HUGE THANKS to*
• Product: <@U03AME5740K|Chima Okechukwu> <@U06QRS4SEBC|Rianna Schanno> 
• Design: <@U02TP8JFQ4Q|Chris Keimig> <@U03K5MLFBS4|Chris Sywassink> 
• TPM: <@U02KZTXSPTK|Erica Jones> 
• Analytics: <@U02R9QUKXUL|Shakib Ahmed> <@U03A5T1UH4M|Matthew Hendler> <@U0928GRQ65V|Luke Puglisi> 
• Engineering: <@U03C6DP87PF|Mostafa Derakhshan> <@U093RNNE0MQ|Mahshid Zandian> <@U0775UBDL3T|Vessy Shestorkina> <@U06PSKLD0F5|Anastasia Arnold> <@W8FQB94DB|Ravi Channapati> <@W8GN4BUBH|Danh Dang><@U060RFM8D27|Kranthi> and the <!subteam^S063NQFRQSU> team.
• Marketing: <@U02KM9R6R8A|Danielle DeSarzant> 
• Growth team: <@U09MBAJRP45|Midori Chikamatsu> <@U08Q4H23Y6P|Jay Shah> <@U08ETVD4YTV|Alex O'Reilly> 
Thread: 1 replies (latest: 2026-01-12 13:59:45 PST)
Reactions: rocket_launching (16), fire (8), +1 (2), +1::skin-tone-4 (1)
Files: image.png (ID: F0A8NNTP1DX, image/png, 1.2 MB), image.png (ID: F0A8NNYTNLR, image/png, 2.9 MB)



---

=== Message from Sonia Singhal (U07NYJQUDS8) at 2026-01-13 11:15:01 PST === 
Message TS: 1768331701.159239
:drum: :rocket:  *Launched: Agentic QnA in Product Support Agent for Mailchimp* :intuit-assist-thinking:

:rocket: *What we launched*
 We’re excited to announce that we have launched *Agentic QnA (AQnA)* inside the *Product Support Agent (PSA)* to *100% global traffic* for *Mailchimp Product Support*. This is a transformational experience where digital help in MC becomes context aware, config driven.
This replaces the prior *HelpGPT* experience for *GenAI-routed product support* and evolves the Mailchimp Digital Assistant from a simple LLM response into a *config-driven, agentic support experience*. We can now *control, tune, and scale* it.

With *PSA + AQnA*, Mailchimp customers now get:
• *Smarter disambiguation* that asks targeted follow-ups instead of guessing
• *Multi-turn, in-session memory* so customers don’t have to repeat themselves
• *Clear, product-aligned guidance* that maps cleanly to Mailchimp flows
• *Guardrails + feature gating* to avoid irrelevant steps and dead ends
• *RPP retrieval* for more grounded, consistent answers
• *A* *modular, config-driven framework* that makes it easy to add and scale curated intents over time
:muscle: *Why this matters*
*From (HelpGPT):* HelpGPT often returned generic steps, lost context on follow-ups, and struggled with topic shifts.
*To (PSA + AQnA):* PSA + AQnA delivers a more agentic, context-aware experience with better disambiguation, cleaner topic switching, and more complete guidance. It remains controllable and scalable through configuration.
*Example*
• *Customer:* “How do I increase the open rate for my campaigns?”
• *Before (HelpGPT):* “Improve your subject line, segment your audience, avoid spam words, and test send times.”
    ◦ *Customer:* “What should I change in Mailchimp?”
    ◦ *HelpGPT:* Repeats generic advice without narrowing down campaign type, audience setup, or what the customer can actually do next in-product.
• *After (PSA + AQnA):* “Happy to help. Are you trying to improve opens for a regular email campaign or a Customer Journey email?”
    ◦ *Follow-ups (targeted):* “Which audience is this going to?” “Is this a new campaign or are you optimizing an existing one?” “Do you have a recent campaign we can use as a baseline?”
    ◦ *Guidance (product-aligned):* PSA + AQnA then routes into the right Mailchimp flow, for example: where to review performance, how to compare subject line results, how to segment the audience based on engagement, and how to test send time or subject lines using the right in-product options, while avoiding steps that do not apply to the customer’s setup.
*Impact*
• *Interaction rate :* 72% → 80%:ddr-up:
• *Answer rate* - ~70% - 90% :ddr-up:
• Accuracy(manual evals) 91%
• Relevancy(manual evals) 93%
:fast_forward: *What’s next*
• Add *HHO agent* for human handover support
• Scale more *curated intents* into AQnA and *increase GenAI traffic safely*
• Expand *PSA + AQnA* coverage across additional Mailchimp support entry points
• Auto Evals
:raised_hands: *Thank you*

This milestone happened because of strong cross-team collaboration across product, engineering, platform, and design.
Special shout-out to *<@U05HF187G14|Krithikha Balamurugan>, <@U02KM5B3LCT|Brett Belcher>, <@U02KEED6LTG|Ankur Bag> and <@U02LB7CQ0EL|Will Greer>* for the rigor and dedication that made this launch possible.

*Agentic QnA:* <@U05HF187G14|Krithikha Balamurugan> <@U07NJNRFF4N|Gurukiran V> <@U05SB37CEG1|Alakesh Bora> <@U09C7FBSXCJ|Anshul Singhal> <@U0866UZBCS1|Arpita .> <@U01UPTKJ81E|Swastika Tiwari> <@U08H5ACAN3E|Indrajeet Das> <@U09E3E3UK54|Nitin Raghunathi>
*PM Drivers:* <@U07NYJQUDS8|Sonia Singhal> <@U03ELQLTRGR|Ziv Shtacher Heimlich>
*Mailchimp milestone team:* <@U02KM5B3LCT|Brett Belcher> <@U02LB7CQ0EL|Will Greer> <@U02KEED6LTG|Ankur Bag> <@U07NYJQUDS8|Sonia Singhal> <@U02KJCQGWQ5|Leanna Popp> <@U02LATJSU2U|Anna Kelley> <@W8FL2R1J6|Roopesh Sheth> <@U02KJ3JU2LV|Alvaro Bueno>  <@U039RUNMK25|Tan Le-Dang> <@U01RM6L084A|Sara Mikulic (she/her)> <@U02KMCS68BC|Lisa Highfill> <@U02KM5HSV99|Caleb Childers (he/him)>
*VEP AI:* <@U06D7QHA5NU|Fae Salehi Amiri> <@U094JHXDDRD|Manideep Reddy> <@W8F0S62N4|Niraj Patel> <@U07TG2ZFPEG|Perez Ogayo>
*Agent Framework:* <@U01Q51BEH6V|Sam Watson> <@U01MW4J7GCQ|Adam Sidiali> <@WFX91FPV1|Parker Westfall> <@W8F0QCY7J|Francis Cullen> <@W8GG92L5U|Trever Cullen> <@U02MRFNH6SF|Alex Zharkikh>
*TPM:* <@U02P3E24VSM|Nancy Joseph Soris> <@U01FS2T6H6Y|Karthik Chandrasekaran>
*Architects:* <@W8F0QCS3A|Ken Yocum> <@W8FL2SDLJ|Paul Hubbard> <@WG4K2EBK3|Manasa Yogeesh>
*Analytics:* <@WT7TPT0AU|Akshay Kher> <@U03MZUB79C4|Shinny Jain> <@U01RJ6XJY5N|Noel Fernandes>
*Leadership:* <@U03KWGUK8D6|Julie Zimmerman> <@U02KJG17Q0M|Tanisha Barnett> <@W8FQBGE2Z|Hema Narasimhan> <@WBJKM2HA6|Gabriele Pansa> <@WH0PS8H99|Adi Shalev> <@W8GG8A97G|Sandhya Kummara> <@WP2LWEK53|Pritesh (Tesh) Desai> <@W8FL4PR2N|Praveen Kulkarni> <@WD2NV323H|Julia Daher> <@U069B9ZM7UG|Abhishek Jain> <@W8FHWDUUB|Wendy Anderson> <@W8FHXM3PD|Harindra Katkam> <@W8GG65CDC|Nagaraj Janardhana> <@W8FMAF05A|Rajshekhar Desai> <@W8FMBV9NG|Nivi Kumar> <@U03RFH35EJD|Agnita Pandian> <@W8FMAH2VA|Nikos Ioannou> <@W8FM8UQBE|Sumit Choudhary> <@W8F0QKA48|Luiz Faria> <@U09NCTVAJ6B|Alexandre Alves> <@U06QXSVC83U|Jason Brightman - 510-735-5794> <@U01JKQ9BB9C|Shilpa Reddy (she/her)> <@WH3P9023S|Lance Williams - 408-477-0444>
Reactions: clapping-all (13), heart (5), +1 (2), purple_heart (1)
Files: AgenticQnA IN product support agent IN mailchimp video (4).mp4 (ID: F0A8W7WHG1X, video/mp4, 12.5 MB)



---

=== Message from Payton Camilli (W012EU6L7FG) at 2026-01-14 14:39:44 PST === 
Message TS: 1768430384.015689
:rocket: *CDP Powered All Contacts Table!!* :rocket: Full release summary <https://wiki.intuit.com/pages/viewpage.action?pageId=1478154973|here>.

:question2: *What changed?* The All Contacts table now pulls contact data from CDP instead of the monolith (with the exception of tags and interest groups)

:clap-clap: *Why is this a big deal?*
    ◦ Giant performance improvements on initial page load for our highest value customers (P99.99). We've observed:
        ▪︎ 78% decrease in users waiting more than 5 seconds for the table to load
        ▪︎ 91% decrease in users waiting more than 10 seconds for the table to load
    ◦ Brings us one step closer to fully leveraging the centralized contact data from our single source of truth (CDP)
:books: *Resources*
    ◦ <https://docs.google.com/document/d/10-tl61ng3a6FWPkjugCITb0T5OXYVSIqGRP-atKTlko/edit?tab=t.0#heading=h.jzfvhduieew2|PRD>
    ◦ <https://mailchimp.splunk.intuit.com/en-US/app/search/cdp_all_contacts_performance?form.field1.earliest=-72h%40h&form.field1.latest=now&form.field2=*|Splunk>
:next: *Whats next?*
    ◦ Inline contact search experiment (<https://docs.google.com/document/d/1rRvr6olmHxOj8bt6QhnB9M8XMjN-3ehuc0rq3XgwDcQ/edit?tab=t.0#heading=h.4c40og9ra3k3|PRD>)
    ◦ Enabling sort for all users on all merge fields, regardless of list size
    ◦ Sorting contacts within a segment view
:mega: *Who made this possible?* :mega:
    ◦ *Audience team:* <@U02KM4PQQQ3|Alli Shepherd> <@U02KZQ945CH|Carlton Freeman> <@U03FZ581XTR|George Nakkas> <@U02KMC4S798|Khadijah Parks> <@U07ACBL1WAY|Lavanya Malladi> <@U063VQYDNQ5|Livia Gimenes> <@U05G24X48C9|Mario Merendino> <@W012EU6L7FG|Payton Camilli> <@U07USKD0MA5|Shefali Dalal>
    ◦ *CDP:* <@U078B7PT3A8|Dan Damkoehler> <@WP0ENL12Q|Deepak Mirani> <@WA3PKCN66|Jessica Lin> <@W8FL3HEMQ|Navjot Cheema> <@U04SC218QQ3|Sijia Liu>
    ◦ *Leadership:* <@U09QF7F45AQ|Nathan Snell> <@W8FHXCZSP|Saikat Mukherjee>
Thread: 5 replies (latest: 2026-01-14 18:39:43 PST)
Reactions: yellow_heart (24), rocket (25), cdp2 (12), cooldog (10), fire-ball (12), clapping-1772 (3), raised_hands (1)



---

=== Message from Laurie McGowan (U02KMCPC99R) at 2026-01-15 07:08:09 PST === 
Message TS: 1768489689.533599
*As Matt mentioned in yesterday's Huddle reminders, the Mailchimp Innovation Council (MIC) is getting together again - virtually this time!*

Last September we kicked off the MIC with an in-person, 2-day event at our Atlanta HQ. In it, we gathered a ton of foundational insights across Agentic AI, Omnichannel Strategy, Platform Feedback, Partner Experiences, and Insights & Reporting.

:product-insights: _Check out our <https://docs.google.com/presentation/d/1uJNzSLKtrEfTrBZ5ZD4wAqSwNPZQe6MtmtIdaDMjZGM/edit?slide=id.p#slide=id.p|takeaways one-pager> or dig into the <https://docs.google.com/presentation/d/13JYXM72T4tdUx_XV3G25Xu1v02dfvJmAZIfRJsXvNo0/edit?slide=id.g34532690c16_1_2275#slide=id.g34532690c16_1_2275|full takeaways here>._

Now we’re excited to “get the group together again.”  We’re hosting an extended, 2-hour virtual session that centers on Automations and Segmentation insights. There is a ton of cross-team work being done in H2 that touches significantly on these areas, and we can’t wait to get their perspective.

_How can I participate?_

We’ll host this session on *Tuesday, January 27 from 10-12pm ET*, and we’re inviting anyone across our org to <https://docs.google.com/forms/d/e/1FAIpQLScgNeiE4WERtlFOrwTbjT7cnl6c4AZHXkL-Hr3jK3e3OJTxKw/viewform?usp=dialog|sign up and listen live>! By signing up, you'll receive a calendar  invite and be added to our Slack channel for more details.

:point_right: *<https://docs.google.com/forms/d/e/1FAIpQLScgNeiE4WERtlFOrwTbjT7cnl6c4AZHXkL-Hr3jK3e3OJTxKw/viewform?usp=dialog|Sign up> by Friday January 23!*
Reactions: yellow_heart (9), tada (7), celebrate-incl (7)



---

=== Message from Connor Callahan (U02KPE15PCL) at 2026-01-21 07:58:35 PST === 
Message TS: 1769011115.402179
:sms: :rocket: :landed2:  *Launched and Landed | Add SMS Creation to Email Creation Checklist*
The *SMS Growth team* & <#C03TDDSMLR4|mc-messaging> is stoked to share the results from our persistent toggle test which has improved SMS bookings by 139% for a forecasted in-year impact of $450k.

:test_tube: *Problem & Hypothesis:* The only mention of SMS in the core email creation flow was a lone IPD driving <50 SMS bookings per month. We hypothesized that by exposing users to Mailchimp SMS in context of the email they are sending, we would build their mental model of Mailchimp being an omni-channel platform and increase their propensity to purchase SMS by at least 100%. After this test we were driving an average of ~440 new bookings per month.

:boom: *Impact*
• A *<https://docs.google.com/presentation/d/15W4xkqX6I0_BVV8I0z5_fWT17DlkX_eoJjHIqBuiClY/edit?slide=id.g3b2cf356b59_5_869#slide=id.g3b2cf356b59_5_869|+139%>* :updates: *novelty adjusted increase* in *New SMS Bookings*
• *In year* :updates: *$450k increase from New SMS Bookings*
• *A <https://docs.google.com/presentation/d/15W4xkqX6I0_BVV8I0z5_fWT17DlkX_eoJjHIqBuiClY/edit?slide=id.g3b2cf356b59_5_869#slide=id.g3b2cf356b59_5_869|28%>* :updates: *increase in SMS Campaigns Sent*
:product-insights: *Learnings (1) The value of default to Omni* :e-mail::calling::  When we iterate with empathy - like adding toggle persistence and refining the UI based on feedback - we aren't just "pushing" a feature; we are reducing cognitive load and helping customers discover the more effective ways to reach their customers. *(2) The value of the speed to learnings* - We released experiment <https://docs.google.com/document/d/1g_vkJloJkT5iKbmxRatnD96wzY1_Yb7W9NoXNWr1ObA/edit?tab=t.0#heading=h.4c40og9ra3k3|x256 EDD> on 12/3, saw very positive results accompanied by negative VOC around the toggle. The team rallied and within two weeks designed, developed and shipped <https://docs.google.com/document/d/1rxFBYj8K-gccWuFzIdZFmOB_obeuoQs8jMq6HSho9-Y/edit?tab=t.0|x284 EDD> just before HCAP giving us the ability to call results the week upon returning from break, maximizing the in-year impact.

:extreme-teamwork: *Many thanks:* SMS Growth Team & Irrational Labs: <@U02KM1TUH8B|Ashley Lawrence> <@U09LGAM2PHT|Arpit Parekh> <@U098480GM26|Minal Rivonker> <@U02QFTEHKB9|Kevin Martin> <@U09FFNUCUTD|Harrison Neuert> <@U05DS9303MX|Jeff Ott> <@U02KMCXQJ7M|Kelly Hale> <@U02KEHAB5U6|Claudia Majors> <@U0970UUFN80|Ashish Prakash> <@U02KJF76MU5|Rujuta Apte> <@U02KJEHK677|Neil Desai> <@U02KPE15PCL|Connor Callahan> Exec Sponsors: <@U0884DN8VGV|Matt Idema> <@U08KK7S6LAZ|Diana Williams> <@W8FHYGK19|Jack Tam> <@U07AX5J7MFB|Eric Anderson> <@W8F0RNH4Y|Nathan Bullock>
Thread: 3 replies (latest: 2026-01-21 15:01:38 PST)
Reactions: clapclap (29), wow-frog (10), hellyeah-7445 (9), rocket (5), fire (5), wow3 (4), raised_hands (3), letsgoooo (4), raised_hands::skin-tone-2 (1)
Files: Checklist.png (ID: F0A9G186JQ7, image/png, 200.1 KB), Confirmation.png (ID: F0A9VD7U8DC, image/png, 84.2 KB)



---

=== Message from Franco Reyes (U03AQ35Q2P6) at 2026-01-22 13:10:15 PST === 
Message TS: 1769116215.543849
Launched :rocket: :rocket:
_*The Dotcom Funnel Innovation Team*_ rolled out our Mailchimp Assistant (v1.5) experiment to 100% today with no errors, to the *US*, *AUS* and *UK!*! Super excited to finally launch this test :celebrate:

Huugee shoutout to <@U02KEKNFZD4|Jon Wallace (jWall)> <@W8F4XD9U1|Arun Avanathan> <@U02KPL46GDS|Munia Rahman> <@U03SHEV00CU|Nylah Julmice> <@U02KM9USVDY|Greg Clark> <@U03ETSQ5A1K|Jeremy Tillman> <@U02B9R7MAH3|Brian Nguyen> <@U033CC0AUD8|Caroline Josey> <@U02URC9KK46|Lawrence Ma> on their amazing work driving this effort, navigating uncertainty, and collaborating closely with other teams at Intuit. Thank you for your partnership :pray: <@WQQ5MTAHZ|Faizan Hadfa>, <@U01GFNQ5Y85|Cameron Hilton>, <@U0246SZAG13|Lavanya Siva>, <@U04AKTS5X3J|Param Mehta>, <@U03QGS0HHJ7|Aliaksei Minin> and <@U02A36NFLQP|Aruna Ghiware> to make this happen :tada:

:millyrock-986:Congrats <!subteam^S08H2TW4HEE>!! :millyrock-986:

*Runtime:* 1/22 - 2/2
*Primary KPI's:* NB MRR, activations, MQL's, Engagement

As our test runs, the team is making progress on MCA V2 which will introduce our first tool call for accurate pricing info, addition of ongoing response quality monitoring, optimized search page experience, and UX upgrades. Its an amazing start with huge opportunity for improvement :yay:
<@WB6QH3S20|Christine Kuo> <@W9GLZQ45A|Ryan Tuosto> <@U0A99U871KR|Sid Bakhru>
Reactions: rocket_launching (9), raised_hands (4), yay-frog (4), raised_hands::skin-tone-5 (1)
Files: Screenshot 2026-01-22 at 4.09.10 PM.png (ID: F0AAB3137JR, image/png, 50.8 KB), Screenshot 2026-01-22 at 4.09.37 PM.png (ID: F0AB8QJVC7J, image/png, 85.1 KB)



---

=== Message from Rianna Schanno (U06QRS4SEBC) at 2026-01-23 08:01:27 PST === 
Message TS: 1769184087.824189
:inprogress3:*Optimal Business Setup: New Homepage Checklist drove stat sig lift in Completed Actions and Conversions!*

:checklist:We’ve launched a new Homepage Setup Checklist that replaces the task list with a focused, progressive checklist to guide new users through core setup actions—adding contacts, connecting integrations, authenticating domains, and importing a brand. By prioritizing the right actions at first login, this experience helps users reach value faster. :checked:

*Impact & metrics:*
The new checklist drove a statistically significant *5.1% lift in new users completing 2+ setup actions* within 14 days (+121 bps). We also saw a stat sig *+50 bps increase in in-app paid conversion* for new users, representing a 13.8% lift versus control. No negative guardrail impacts observed.

*Huge thanks to everyone who made this possible* :raised_hands:
Design: <@U02TP8JFQ4Q|Chris Keimig> <@U02KEKNRQ4W|Kateryna Smal>
Engineering: <@U03DRMGVA1L|Mary McKeon> <@U03TDGMMFM1|dario_el-badry> <@U045VFLCST1|Jenna Emerman> <@U05Q70X0FQC|Ashley Oelbaum>
Product: <@U035F1N6TLG|Eva Frishberg> _(Irrational Labs Shoutout!!)_ <@U02KM90H7R9|Brittney Muhamed>
Analytics: <@U02R9QUKXUL|Shakib Ahmed> <@U02KEHAB5U6|Claudia Majors>
_And special thanks to all the cross-functional partners who helped ship and review this work!_ 
cc <@U08D0C42PJM|Andrew Spitz> <@U060RFM8D27|Kranthi> <@U03K5MLFBS4|Chris Sywassink>
Thread: 7 replies (latest: 2026-01-23 16:12:31 PST)
Reactions: celebrate (38), clapping-all (24), rocket_launching (25), muscle (3), muscle::skin-tone-2 (2)
Files: image.png (ID: F0AALG4T082, image/png, 243.7 KB)



---

=== Message from Devin Mercier (he/him) (W0132PNAC9X) at 2026-01-27 07:10:58 PST === 
Message TS: 1769526658.697309
:rocket:*Simplification of the Email Checklist Live to 100% of Customers* :dart:

:think_big: *Context & Overview*
For months, our <$299 customers have been telling us the same story: the email checklist feels confusing and full of steps that distract from the core goal of sending a campaign. VOC analysis and UXR studies consistently surfaced "too many steps," "unclear blockers," and "I don't know what's preventing me from sending" as top usability frustrations. This friction was directly impacting Create-to-Send (C2S) rates, a validated leading indicator of churn risk. Users were stalling out, abandoning campaigns mid-flow, and losing confidence in the platform. We hypothesized that by simplifying the checklist structure, reducing non-essential items and focusing users on the five core actions required to send (To, From, Subject, Send Time, and Content), we could reduce cognitive friction, increase clarity, and ultimately improve campaign completion rates.

*We shipped it as an experiment on December 19. After two weeks of data, the results were clear: improved C2S rates from 55.4% to 57.2% (+1.8 ppts), no harm to guardrails, and minimal downside risk. We rolled it out to 100% on January 12.*

:blob_no_problem: *Customer Problem*
*I AM* a small business owner managing my own marketing with limited time and technical expertise
*I AM TRYING TO* set up and send my email campaign quickly so I can focus on running my business
*BUT* the checklist has too many steps of mixed importance, and I can't tell what's actually required vs. optional
*BECAUSE* items like "Add Social Post," "Settings," and "Share" are treated with the same visual weight as "To," "Subject," and "Content"
*WHICH MAKES ME FEEL* overwhelmed, confused, and uncertain whether I'm actually ready to send — leading me to abandon the campaign or delay sending

:rocket: *What Was Launched?*
*We simplified the Email Checklist experience for all email campaign creators.*
What changed:
• *Consolidated the checklist from 8 visible steps to 5 core actions:* To, From, Subject, Send Time, and Content
• *Moved secondary features out of the main checklist flow:*
        ▪︎ "Share" functionality consolidated within the checklist (not a separate step)
        ▪︎ "Settings" moved to the header for easier access without cluttering the checklist
        ▪︎ "Add Social Post" deprioritized as a secondary action
• *Improved visual hierarchy and spacing:* Cleaner layout, reduced scroll length, more consistent spacing, with subject line AI recommendations performing well in the checklist we also decided to remove the broken subject line helper
• *Cleaned up language:* Removed bulky copy that wasn't helping customers complete and send campaigns
Where it shows up:
• Email campaign creation flow (all users, all campaign types)
:chart_with_upwards_trend_intensifies: *<https://docs.google.com/spreadsheets/d/1Qfepw_9MNa46LcdXTBDREA9QMorxqBOJo7Udeb9PqrM/edit?gid=1113122779#gid=1113122779|Metrics>*
_Primary Metric_
• *Avg. Campaign Sends per C1*
    ◦ Baseline (Control): 0.606 campaigns per C1
    ◦ Result (Variant): 0.609 campaigns per C1
    ◦ *Outcome:* Flat / inconclusive, but directionally favorable (90% probability Variant > Control)
_Secondary Metric_
• *Campaign Create-to-Send Rate (C2S)*
• Control: 55.4%
• Varirant: 57.2%
• *Result:* +1.8 percentage points improvement :white_check_mark:
_Guardrail Metrics (No Harm Done)_
• *C1 Campaign Send Rate:* 45.3% (Control) → 45.2% (Variant) — Flat
• *Social Posting Rate:* 2.2% (Control) → 2.2% (Variant) — Flat
:next: *What's Next?*
*This is the first in a series of core usability improvements to the campaign creation experience.*

:shoutout1: *Shout Outs & HUGE THANKS*
This was a true cross-functional effort to ship a customer-centric improvement backed by research, data, and disciplined experimentation.
<@U09B1S1DZ6Y|Sundeep Nadendla> <@U02KZMX4E6M|Celeste Mora (they/them)> <@U02KM32BC67|Alejandra Rodriguez> <@U07RKQ1P8Q2|Yizhou Qiu> <@U02VDDRRUG7|Stephen Tiedemann> <@U03TAMKCM37|Patricia Blackwelder> <@U077N1MCR6E|Bharathi Raja Palaniswamy> <@U04SQQF50DP|Kamrin Kennedy> <@U02KJB6KQ9K|James Howard> <@U02KM9C1V3L|Dalyn Small> <@U04739FF7M5|Adam Williams> <@U02KPGQGSVA|Jason Calhoun>

<https://intuit.enterprise.slack.com/files/W0132PNAC9X/F0A8WCW08AG/image.png|BEFORE> | <https://intuit.enterprise.slack.com/files/W0132PNAC9X/F0A8SQG6LSE/image.png?origin_team=E7AN7J5RP&origin_channel=C03TLJNADSP|AFTER>
Thread: 9 replies (latest: 2026-01-28 15:01:21 PST)
Reactions: clapping-all (27), amazing45 (8), fire (8), heart (3), thankyou1 (3), yes3 (4), nodding (3), extremeteamwork (3)
Files: image.png (ID: F0A8WCW08AG, image/png, 127.5 KB), image.png (ID: F0A8SQG6LSE, image/png, 61.5 KB)



---

=== Message from Kriti Jain (U056VCNEMHA) at 2026-01-29 12:00:51 PST === 
Message TS: 1769716851.831999
:rocket: *Mailchimp Web Performance Update: Q2*
Team, we’ve completed a 3-month push to optimize site performance.

The major win is on *INP (Site responsiveness) that has seen significant improvement, along with gains in LCP (Loading speed) as well* :raised_hands:

:bar_chart: *Site speed improvement (Oct 27th-Jan 27th)*
• *Mobile INP (Responsiveness):* Improved by *27%* (Origin), *16%* (Home Page), and *37%* (Pricing).
       (Current Mobile INP: 463 ms, Desired INP: 200 ms)
• *Mobile LCP (Load Speed):* Improved by *12%* on the Home Page (offset by minor 5-6% declines on Origin/Pricing).
       (Current Mobile LCP: 3424 ms, Desired LCP: 2500 ms)
• *Mobile CLS (Visual Stability):* Held steady at *0.04*—well within the "Good" industry threshold of 1.00 or below.
We've also seen improvements on Desktop overall as well.

:white_check_mark: *Key Work Delivered to move the needle on site speed:*
• *SEO & LLM Readiness:* Optimized the Resource Hub for GEO optimization, making it easier for LLMs to crawl and search the site in all languages.                             
      Immediate Benefit :clap::
• Non-English part of the Resources Hub Library is fully crawl-able since 1/22 for LLM results.
• AI traffic to non-English articles has increased 115% WoW, clicks from Google are up by 21%.)
Other key deliverables:
• *Code & Script Optimization:* Removed outdated code and delayed "heavy" background scripts so the browser can focus on the user first.
• *Smoother Interactions:* Fixed laggy menus, tooltips, and pricing tables to make the UI feel snappier.
• *Early Warning System:* Integrated performance testing into our launch process (Playwright) to catch and fix "slowness" before it reaches users.
:hammer_and_wrench: *What’s Next?*
We're continuing to accelerate on improving the site speed and are currently tackling more optimizations to move the needle on LCP and INP metrics where we have opportunity to improve further with SVG reductions, smooth font loading, and Hero image optimizations.

We are also launching new experiments specifically focused on reducing the payload size on the Pricing page and for optimizing the sign up page loading - so stay tuned!

*For further reading:*
• :page_facing_up: [<https://docs.google.com/document/d/1TfFRqimXshUfs3Yz6PL9D8Wd-Dh411vGcU5KCj4kW08/edit?tab=t.0#heading=h.ix8i7qwkv5w4|Web Performance Strategy>]
• :chart_with_upwards_trend: [<https://docs.google.com/spreadsheets/d/1tJY2dEU8C5JNYKaIFmSMDtVqviHllrWalQdX4uz3-60/edit?usp=sharing|Performance Tracker>]
Huge congrats to the PD team for these high-impact technical wins! :clap-clap:

PD: <@U02URC9KK46|Lawrence Ma> <@W8GN4BUBH|Danh Dang> <@U02KJ6V3LA1|Cody Solomon> <@U02KEQB3DSA|Steven Sloan (Sloan)> <@U02KEKSD2QN|John Nutter> <@U04ALBZD42K|Chris Zeigler> <@U02KPL46GDS|Munia Rahman> <@U063CC72YRX|Haley Barlar>
PM: <@U056VCNEMHA|Kriti Jain>
SEO/GEO: <@U03D8NKE91S|Ellen Mamedov> <@U0447EKNEH2|Kai Blum>
Thread: 1 replies (latest: 2026-01-29 12:29:24 PST)
Reactions: clapclap (10), sonic-fast (2), celebrate (4)



---

=== Message from Matt Idema (U0884DN8VGV) at 2026-01-29 12:19:26 PST === 
Message TS: 1769717966.834159
Congrats team let's keep it up!
Reactions: heart (1), yes3 (1)



---

=== Message from Devin Mercier (he/him) (W0132PNAC9X) at 2026-01-29 12:41:41 PST === 
Message TS: 1769719301.706109
:rocket: *Progress Indicator in Email Checklist Live to 100% of Customers* :pro-gress: 
UXR studies consistently showed users hesitating when checklist completion wasn't clearly visible they couldn't tell what was required vs. optional, what was blocking send, or whether they were making progress toward completion. We hypothesized that by introducing a progress indicator to the email checklist, we could reduce cognitive friction, increase clarity, and ultimately improve campaign completion rates, especially for new users still learning the flow.

:money_blob: *Impact & Metrics:*
The experiment showed a *+9.7% lift in campaigns sent per C1 for first-time users*, with *$90k in retained revenue* from 110 ITC FTU sends. Campaign *create-to-send rate improved +1.6pp* (+11.7% relative lift) for FTUs. Key insight: FTUs created slightly fewer campaigns (2.1 vs 2.3) but sent nearly 10% more - exactly the "finish what you started" behavior we want for onboarding. Guardrail metrics showed no harm to tenured users.

<https://intuit.enterprise.slack.com/files/W0132PNAC9X/F0AC7R10R25/image.png|FROM> | <https://intuit.enterprise.slack.com/files/W0132PNAC9X/F0ABUSYG3M0/image.png|TO>

:shoutout1: *Shout Outs & HUGE THANKS:*
<@U04SQQF50DP|Kamrin Kennedy> <@U09B1S1DZ6Y|Sundeep Nadendla> <@U02KZMX4E6M|Celeste Mora (they/them)> <@U02KM32BC67|Alejandra Rodriguez> <@U07RKQ1P8Q2|Yizhou Qiu>
Thread: 6 replies (latest: 2026-02-04 23:04:04 PST)
Reactions: raised_hands (12), yes3 (6), raised_hands::skin-tone-2 (6), heart (3), raised_hands::skin-tone-4 (2), tada (2), clapclap (3), raised_hands::skin-tone-5 (1), wow3 (2), raised_hands::skin-tone-3 (1)
Files: image.png (ID: F0AC7R10R25, image/png, 1.2 MB), image.png (ID: F0ABUSYG3M0, image/png, 382.7 KB)



---

=== Message from Chris Sywassink (U03K5MLFBS4) at 2026-01-30 14:10:59 PST === 
Message TS: 1769811059.358999
:rocket: *Mailchimp Mobile Update: Usage-Based Upgrade Moments (Plan Usage Indicators)*

:dart: Context & Overview
Mobile customers often manage their audiences and campaigns on the go, but lack clear visibility into how close they are to plan limits. This creates moments of surprise and frustration when limits are hit, interrupts critical workflows, and leads to missed opportunities to upgrade at the right time. To address this, we launched *Plan Usage Indicators on mobile* — a set of contextual upgrade moments designed to make email send and contact usage clear _before_ customers hit hard limits, and to support proactive upgrades without disrupting core tasks.

:bust_in_silhouette: Customer Problem
*I AM* a small business owner using the Mailchimp mobile app to manage my audience and campaigns
*I AM TRYING TO* understand whether I can keep sending emails or adding contacts without issues
*BUT* I don’t see my usage until I’m blocked or charged
*BECAUSE* usage and limits aren’t visible where I manage my audience
*WHICH MAKES ME FEEL* surprised, frustrated, and unsure what to do next

:bulb: What We Hypothesized
We believed that *clear, in-context visibility into plan usage*, paired with lightweight and trustworthy upgrade paths, would reduce frustration and enable more proactive upgrades — without interrupting core workflows or eroding trust.

:rocket: What Was Launched
We introduced *usage-based indicators directly within the Audience workflow* on mobile.
*What shipped:*
• In-context visibility into email send and contact usage
• Progressive states that educate first (“remaining”) and escalate only when limits are reached
• Upgrade paths designed to balance clarity, customer trust, and business outcomes
• Mobile-compliant flows that respect platform constraints while enabling upgrades
:triangular_ruler: *Design reference:*
Figma — Upgrade Moments (Plan Usage Indicators):
<https://www.figma.com/design/aXdQXtdXsWlnbNmORHj4Zc/Upgrade-moments?node-id=253-12819>

:bar_chart: Early Results from iOS (first ~30 days)
• *$19K+ MRR*
• Highest-performing moments:
    ◦ Email Sends Remaining: *+5.32% conversion*
    ◦ Contacts Remaining: *+4.18% conversion*
These results are notable given the required *mobile → web handoff* and suggest that *contextual, usage-based upgrade moments are an effective monetization pattern on mobile*.
:raised_hands: *Shoutouts & Thanks*
Huge thanks to the mobile design and engineering teams for pushing this forward.
Engineering: <@U088TTV7Z2T|Luis Alberto Orrantia Arteaga> (FO), <@U06L6KAUA30|Julian Fordyce> <@U02KEHZ4PHC|Gaby Chacon> <@U03JKJV4RGR|Marcus Moncayo> <@U02KJ63H57X|Chelsea Youmans> <@U02KEM59CCW|Mark Abdelmalak>
Design: <@U02KPCDC752|Aparna Somvanshi> <@U03K5MLFBS4|Chris Sywassink>
Product: <@U079SMT5UTA|Matt Cimino>
Thread: 3 replies (latest: 2026-01-30 14:29:33 PST)
Reactions: yay-frog (13), woo_hoo (8), money_blob (6), mobile-love (5), mobile-frenz (5), mobile (4)



---

=== Message from Nicole Jayne (U02LB4JPAEL) at 2026-02-02 08:24:32 PST === 
Message TS: 1770049472.622349
:rocket_launching:  *Ecomm Predictive Analytics launches to experiment* :ecommerce-segment:
Historically, Mailchimp has helped marketers understand what already happened—opens, clicks, purchases, and revenue. With the launch of Ecomm Predictive Analytics, we are taking our first major step into helping ecommerce marketers use what is likely to happen next to fuel marketing personalization. This sets the foundation of predictive analytics as a growth platform: giving customers foresight into future buying behavior and pairing that foresight with concrete actions they can take to get and grow customers. This new suite of Predictive Analytics uses next-generation AI models to forecast future purchase intent, timing, churn risk, and customer lifetime value across all contacts, including prospects and one-time buyers. These insights are actionable via segments, campaigns, and automations so marketers can act with precision and confidence to drive higher conversion, repeat purchases, and lifetime value.

:sad-customer: *Customer problem:*
I AM an ecommerce marketer running a digital sales-based small or medium business
TRYING TO increase conversions and revenue from my marketing efforts
BUT I don’t know which customers are most likely to buy or the right time to reach them
BECAUSE I lack predictive insights that connect customer behavior to future purchase intent
WHICH MAKES ME FEEL unsure where to focus my campaigns, incentives, and automations to get the best ROI

:crystal_ball: *What was launched?*
This experiment introduces Ecomm Predictive Analytics, a next-generation, end-to-end predictive intelligence suite that represents a significant leap forward from Mailchimp’s legacy CLV and Likelihood to Purchase models built over a decade ago. It expands Mailchimp from retrospective analytics into forward-looking intelligence, delivering materially higher coverage and accuracy. These predictions meet feature parity with Klaviyo, while going further to deliver superior prediction coverage of subscribers earlier in the buying cycle thanks to the inclusion of richer signals like AI-driven email understanding. Key improvements and capabilities include:
• *Next-gen AI predictive models:* Rebuilt from the ground up using richer behavioral signals—including browsing behavior and AI-detected engagement with promotional vs. educational content—delivering materially higher predictive accuracy 
    ◦ *Likelihood to Purchase*: Predicts how likely each contact is to make a purchase in the next 60, 90, or 365 days, using behavioral signals like browsing, purchases, and AI-understood engagement with promotional vs. educational content
    ◦ *Predicted Next Order Date*: Forecasts when previous purchasers are most likely to buy again, enabling timely and proactive outreach
    ◦ *Predicted Churn Risk*: Identifies customers at risk of not purchasing again, categorized into High, Medium, and Low risk
    ◦ *Predicted Customer Lifetime Value (CLV)*: Estimates the future value of each customer based on likelihood and expected purchase value
• *End-to-end activation*: All predictions are delivered via a new Reporting dashboard in Conversion Insights and available as omnichannel Segment conditions. Next Order Date and Churn Risk are available as Automation triggers to reengage customers 1:1. Individual C2 predictions will be available on Contact Profiles for GA launch.
:product-insights: *From → To*
• Limited, siloed predictive insights → A comprehensive, next-gen AI predictive analytics suite
• Predictions only for repeat purchasers → Predictions for all contacts, including prospects and one-time buyers, +300% C2 coverage increase
• Order-history-only signals → Richer intelligence using store browsing behavior and AI-detected email content engagement, +75% accuracy improvement
• Static insights with unclear next steps → Actionable predictions embedded directly into campaigns, segments, and automations
• Guesswork about who to target next → Clear guidance on who to prioritize, how to personalize, and when to act
:experiment: *What will we learn?*
This experiment will measure whether making a suite of predictive intelligence models available to ecommerce marketers drives more meaningful product actions—such as creating segments, launching campaigns, and starting automations. Our hypothesis is that surfacing predictive insights at the moment of decision-making will lead to smarter targeting, higher engagement, and an increase in the marketer’s share of Mailchimp-attributed revenue through more relevant and timely messages. Results will be coming in hot 2/9

:next: *What’s next?*
Mailchimp will extend our predictive intelligence suite into covering product- and promotion-level predictions, once again knitting together contributions from Reporting & Analytics, Segmentation, Automations, and adding the Email team to deliver dynamic content. These models will sharpen behavioral profiling of each subscriber, including *Next Best Product, Product Affinity and Promotion Sensitivity* that enable strong ecomm-centric marketing personalization that finally closes competitive gaps.

:shout-out: *It truly takes a village*
AI Science: <@U061L1N8EQN|Mary Coffey> <@U06MY7FV9R7|Matt Mills> <@U0793KXBF51|Bryan Smith>
MLE: <@U054QT37B1C|Chaitanya Pantar (CP)> <@U02KEA58ZNJ|Akhila Podupuganti> <@U04QHDJE5RT|Matt Turner>
CDP: <@U07GRQTTY30|Arkesh Rath> <@U04NGRG0RH9|Lauren Colwell> <@U01QDJNG3QX|Jake Langley> <@U04QNS5KEE6|Ajeet Seenivasan>
Reporting & Analytics: <@U0372SDKQDS|Tiffany Huang> <@U0580HUFQ00|Scott Adams> <@WAHLSUUDV|Minh Phan> <@U09E76WKB7B|Surendar Dharani> <@U09RBTL7F47|Praveen SB> <@U0428EDN518|Nick Boyle> <@U03EEL3PU9H|Sid Kumar>
Automations: <@U06QWR7FV9T|Elizabeth Bertasi> <@U02P9STSQGZ|Becca Walsh> <@U03GVFDGUKA|Cliff Martin> <@U09BAMA1N9X|Nakul Lahoti>
Segmentation: <@U04TFSEP31D|James Sheridan> <@U04TWCYUZAN|Mason Hadeler> <@U0603HL0L2E|Denys Salamatov> <@W019Y5V05UG|Mohammad Habbab> <@U03KUBTCSG1|Frank Persico> <@U035AGFSBRC|Sabrina Harris> <@U07USKD0MA5|Shefali Dalal>
PMM: <@U03HRFYTYUB|Simone Kovacs>
Data Science: <@U06EYRJLPMX|Vicki Borja Jennings> <@U08J8FFFVAL|Stam Paterakis> <@U0970UUFN80|Ashish Prakash> <@U07ED705DHS|Aastha Sehgal>
Leads: <@W8FHXCZSP|Saikat Mukherjee> <@W8Z8R7STE|Nir Harel> <@W8FL6URHQ|Deepak Prabhakaran> <@U02KPGZ4HHS|Jane Guthrie> <@U064FLW0QAK|Taylor Horton> <@U09QF7F45AQ|Nathan Snell>
Thread: 10 replies (latest: 2026-02-03 13:27:18 PST)
Reactions: tada (33), crystal-ball (11), lets_go (12), raised_hands (3)

---

=== Message from Vivian Wang (U06UL7W90LS) at 2026-02-03 11:58:14 PST === 
Message TS: 1770148694.688549
:chart_with_upwards_trend: *EXPERIMENT: Marketing Dashboard Reimagined (Outcome-Focused & Automations Data)* :bar_chart: 

1 in 3 SMBs say that understanding what is working is their top marketing challenge. While marketers aspire to be data-driven, data is often fragmented across individual reports, making it hard to compare "apples to apples."

Today, we are closing that gap. We have launched a next-generation analytics experience designed to transform data from passive reporting into active, strategic enablement. The new, reimagined Marketing Dashboard acts as a strategic dashboard, delivering deep omnichannel insights and recommended actions that explain what happened and exactly what to do next.

:eyes: *See the new Marketing Dashboard for yourself here!*
*<https://us12.admin.mailchimp.com/analytics/marketing-dashboard/?experiments=reporting-marketing-dashboard-reimagine:variant>*

:busts_in_silhouette: *Customer problem*
• I AM an Ecomm marketer.
• TRYING TO understand how my marketing is performing and what I should do next to drive business outcomes and revenue.
• BUT I don’t have visibility into the ongoing ROI of my campaigns and automations, nor the strategic guidance to connect activity to results.
• BECAUSE performance data is often buried across siloed reports and lacks isolation to specific date ranges, making it hard to prioritize impactful actions.
• WHICH MAKES ME FEEL unsure if I am allocating my time and budget effectively or if it’s even worth maintaining complex, "headache-inducing" automations.
:rocket: *What was launched?*
This first milestone introduces an outcome-focused dashboard for Standard+ users that integrates automation performance alongside traditional campaigns:
• Conversion-Centric and Engagement-Centric Metrics: Interactive data wells prioritize business outcomes like Revenue, Orders, and Order Rate to reinforce the value marketing drives for the organization.
    ◦ Benefit: Customers can connect the dots between campaigns and their performance to directly understand the business impact of their marketing efforts.
• Unified Automation Visibility: For the first time, flows and (email) automations are integrated into the main dashboard components and filters, allowing users to see how their marketing efforts contribute to engagement and conversions.
    ◦ Benefit: This provides complete visibility into the revenue generated by always-on marketing, allowing users to justify their investment in complex automation flows.
• Campaign-Level Visualizations: The "Performance Over Time" chart is replaced with a campaign-by-campaign breakdown, allowing for faster diagnosis of which specific creative executions drove results. We’ve introduced a granular campaign-by-campaign breakdown that allows for instant "apples-to-apples" comparisons.
    ◦ Benefit: It delivers an actionable diagnosis of “what works.” Marketers can quickly identify winning creative patterns and replicate them to optimize future sends.
• Guided Actions & Insights: Recommendations such as Replicate Campaign or Create Active Core Segment provide clear next steps based on performance trends.
    ◦ Benefit: This turns data into immediate action. It removes the "burden of analysis" from the marketer, providing a clear path to their next best move.
• Trustworthy Data Quality: Built-in bot filtering and enrollment in our new data quality framework ensure all metrics are accurate and complete.
    ◦ Benefit: Marketers can make decisions with confidence, knowing their insights aren't skewed by non-human activity or fragmented data sets.
:new: *From* → *To*
• Single-Channel Views :arrow_right: Unified Omnichannel Insights: Connect data across Email and SMS to support multi-channel first marketing.
• Campaign-Centric Metrics :arrow_right: Business Outcome-Oriented: Shift focus from clicks to revenue, conversions, and site activity.
• Passive Monitoring :arrow_right: Strategic Next Steps: Move from static charts to actionable recommendations that suggest the next move.
:brain: *What will we learn?*
This experiment will measure the Insight to Action rate, seeking a lift in meaningful product actions such as automation optimizations, segment creation, and campaign sends. Our hypothesis is that providing a centralized, outcome-focused view will enable marketers to make faster optimization decisions and drive stronger performance.

:1234: *Experiment & Success Metrics*
This launch is a dedicated experimental milestone for Standard+ users. Our goal is to share learnings on how this dashboard drives performance before moving fully into Q3 work.
• Primary Success Metric: Insight to Action (Email Sends)
    ◦ We are tracking email sends as the most important signifier of retention. We will measure:
        ▪︎ Average Campaigns: Sum of sent email campaigns per user who visited the dashboard (filtering for outliers).
        ▪︎ Activation Rate: Percentage of users who send 1+ campaign during the experiment after visiting the dashboard.
• Learning Metric: Share of Total Attributable Revenue To measure customer benefit, we are monitoring the % of revenue attributed to Mailchimp (Mailchimp attributed revenue / Total revenue). 
:black_right_pointing_double_triangle_with_vertical_bar: *What’s next?*
We will focus on helping marketers dig deeper into their data with the MC AI Analytics Agent and LLM-powered actionable insights. These features will significantly expand access to the detailed breakdowns that diagnose why a metric is moving, and tee up the user's next course of action based on that analysis.
• MC AI Analytics Agent: We foresee using the agent to allow users to ask follow-up questions about the specific data they see on their dashboard (e.g., "Why did my revenue spike last Tuesday?").
• LLM-Powered Actionable Insights: We will evolve our current guided actions into highly personalized, LLM-generated recommendations. These will move beyond generic prompts to offer specific strategies tailored to the user's current marketing situation and diagnostic performance data.
:muscle::skin-tone-3: *Shout outs*
• Product: <@U06UL7W90LS|Vivian Wang> <@U02LB4JPAEL|Nicole Jayne> 
• Design: <@U0372SDKQDS|Tiffany Huang> 
• Eng: <@U03EEL3PU9H|Sid Kumar> <@U07U8BJH8R0|Manjusha> <@U02K6PD6HN3|Michael Heard> <@WK626SJMC|Sudeepta Das> <@U03ALF0U1GR|Carson Britt> <@U071H9QQZ7F|Alexandria Cassagnol> <@U06N61JMF6K|Vishwanth Jonnagadla> <@U09RWU1AAR2|Sivaram Ramalingam> <@U09LGBAMWSD|Aravindhan Sivaraman> <@U02KMECQYRY|Paco Orozco> <@U09RBTL7F47|Praveen SB> <@U06U846AJFJ|London Baker>
• CDP: <@U04NGRG0RH9|Lauren Colwell> <@U04QNS5KEE6|Ajeet Seenivasan> 
• PMM: <@U03HRFYTYUB|Simone Kovacs> 
• Data Sci:<@U0970UUFN80|Ashish Prakash> <@U07ED705DHS|Aastha Sehgal>  <@U06EYRJLPMX|Vicki Borja Jennings> 
• Leads: <@W8FL6URHQ|Deepak Prabhakaran> <@W8FHXCZSP|Saikat Mukherjee> <@W8Z8R7STE|Nir Harel> 
Thread: 1 replies (latest: 2026-02-03 13:00:54 PST)
Reactions: itsbeautiful (8), rocket (13), chart_with_upwards_trend_intensifies (7), dance_girl (2)
Files: Screenshot 2026-02-03 at 11.44.16 AM.png (ID: F0ACAQC3V6K, image/png, 286.6 KB), Screenshot 2026-02-03 at 11.47.44 AM.png (ID: F0ACKSP04RZ, image/png, 129.8 KB), Screenshot 2026-02-03 at 11.44.23 AM.png (ID: F0AD56EB7R7, image/png, 184.0 KB)



---

=== Message from Alex Vovk (U063JM5UW5P) at 2026-02-04 13:49:01 PST === 
Message TS: 1770241741.319809
:rocket_launching: *MC Search CDP Migration*

*What did we launch?*
Mailchimp's search infrastructure has been successfully migrated from legacy Elasticsearch clusters to the Customer Data Platform (CDP), modernizing the backend that powers contact and campaign search for millions of users daily.

*Why is this important/beneficial?*
:moneybag: *Big Cost Savings*
This migration is a critical step toward Mailchimp's datacenter consolidation initiative, which will enable $3 million in annual savings from shutting down the legacy search & segmentation colo infrastructure. This project removes one of the key blockers to decommissioning the datacenter.

:rocket: *Future-Ready Infrastructure*
By migrating to CDP's modern OpenSearch infrastructure, we've built a solid foundation that enables the Search and Wayfinding team to deliver enhanced search capabilities and new features more efficiently.

:zap: *Better Performance & Scale*
The new CDP-powered search infrastructure provides improved indexing speeds and the ability to scale seamlessly as Mailchimp's user base continues to grow.

:dart: *Strategic Modernization*
This migration is a critical milestone in Mailchimp's infrastructure modernization initiative, replacing end-of-life Elasticsearch clusters (decommissioning deadline: February 2026) with cutting-edge technology that positions us for long-term success.

*Who is impacted?*
All Mailchimp users who utilize search functionality to find contacts, campaigns, and navigate the product.

*What changed? Describe from/to*
*From:* Search powered by legacy Elasticsearch clusters in colo, populated by PHP consumers and Kafka streams managed by the Segmentation team.
*To:* Search powered by CDP OpenSearch infrastructure, utilizing modern data pipelines with improved indexing performance and query capabilities.

*Success Metric*
Search engagement rate (percentage of users who perform a search and click on a result) <https://app.amplitude.com/analytics/intuit-portfolio/chart/wocfpi8f/edit/40dg142u>

*What's next*
The team will continue monitoring search performance metrics and user engagement to identify opportunities for optimization. With the modern CDP infrastructure in place, future enhancements to search relevance and new search capabilities can now be developed more efficiently.

Slack Channel: <#C03TYAXTLTT|discovery-search-experience-eng>
PRD: <https://docs.google.com/document/d/1DaKmjVe0xgMIpN-nNJK624WPJGLj65OqtMejjdUwX18/edit?tab=t.0#heading=h.1926r9m1hkeb>
Results: All search metrics <https://app.amplitude.com/analytics/intuit-portfolio/dashboard/ntk2apng>

:team:  *Team*
<@U02KMAX8QUT|Jason Veatch> <@U02LZSZN9J8|Samuel Barksdale> <@U063JM5UW5P|Alex Vovk> <@U069GKEGQ90|Jason Lin> <@U05UAN7K3S9|Dharmesh Solanki> <@WA3PKCN66|Jessica Lin> <@U078B7PT3A8|Dan Damkoehler> <@U0A4STXC88K|Praneethi Komatreddy> <@U086AEY40BF|Chethana V P> <@U02LB7537J4|Zac Wall> <@U02KZTXSPTK|Erica Jones> <@U060RFM8D27|Kranthi>

cc. <@U06K8UTTSJE|Jing Wang> <@W8GN4BUBH|Danh Dang>
Thread: 14 replies (latest: 2026-04-09 21:42:13 PDT)
Reactions: rocket (18), awesome-star (9), party-cat (7), clapclap (5)
Files: image.png (ID: F0AD21EDWRY, image/png, 283.6 KB), image.png (ID: F0ADEV6NDTK, image/png, 283.5 KB)



---

=== Message from Payton Camilli (W012EU6L7FG) at 2026-02-05 16:06:36 PST === 
Message TS: 1770336396.700909
:sun2-2908: *SUNSET - The Audience Dashboard* :sun2-2908:

:question:*What changed?* The audience dashboard has been fully sunset!

:clap-clap: *Why is this a big deal?*
    ◦ Once upon a time, there were three audience related dashboards - the audience overview, the audience dashboard, and the audience analytics page. They all had overlapping information, but the data was often out of sync, causing user mistrust. 
    ◦ The audience overview has already been sunset, so with the sunset of the audience dashboard, *the Audience Analytics page is now the source of truth for contact analytics*. 
    ◦ All bugs related to this page can be marked as `won't do`
:books: *Resources*
    ◦ <https://docs.google.com/document/d/1EgO99KC2ozTh54G-O4_rpvy0jleUPR2peoGGWHhhxM0/edit?tab=t.0#heading=h.atzvqrd3cnlm|Audience Dashboard Sunset Plan>
    ◦ <https://docs.google.com/document/d/13oDb4mzmjwLsfPL3OGZ8K7wNWRhoV0b_YSWTLVxU0kE/edit?tab=t.0|Wayfinding EDD>
:next: *Whats next?*
    ◦ <https://docs.google.com/document/d/15ZfyNh9RzXJbyr97mJ0ZkMb4M6fcR02zmNXiIdwMbYA/edit?tab=t.0#heading=h.nfx9atj68jaz|Sunset predicted demographics> (<@U02LB4JPAEL|Nicole Jayne>)
:mega: *Who made this possible?* :mega: This effort has changed hands many times, but special shout-out to the following teams!
    ◦ Audience team
    ◦ Analytics team
    ◦ Segmentation team
    ◦ Wayfinding team

Thread: 1 replies (latest: 2026-02-05 16:07:44 PST)
Reactions: clapclap (20), sunset (6), salute2-4770 (2), pouroneout (1)



---

=== Message from Connor Callahan (U02KPE15PCL) at 2026-02-06 07:59:24 PST === 
Message TS: 1770393564.398149
:sms: :rocket: *Launched  | Agentic SMS Follow-up Campaign Recommendation (x259)* 

For 37% of Mailchimp customers, choosing the right channel and content is a top-3 marketing challenge. In SMS this is felt hardest where *<https://docs.google.com/presentation/d/1fqFDaWwQDre6_Zf5_XEum3uJjtj7wirLkXYYIaIths8/edit?slide=id.g3529b30839a_0_1902#slide=id.g3529b30839a_0_1902|76%> of SMS C1s have no SMS marketing experience*. When people abandon the SMS application, the *<https://docs.google.com/presentation/d/1fqFDaWwQDre6_Zf5_XEum3uJjtj7wirLkXYYIaIths8/edit?slide=id.g3529b30839a_0_1803#slide=id.g3529b30839a_0_1803|#1 barrier is strategy>*, and when pressed, they share their <https://docs.google.com/presentation/d/1fGgXBLEUGXDGaf2FG_IJAjyV-5lnmZzn8DXzYDgDrI4/edit?slide=id.g26c67e91e14_1_47#slide=id.g26c67e91e14_1_47|biggest challenge> is creating valuable content.

With this release, we meet our customers in their moment of highest intent with an agentic recommendation that converts their email into a *contextually relevant* and *personalized* SMS follow-up. This takes the guesswork out of *crafting valuable content* and an initial *Omnichannel strategy.* 

:sparkles: *Highlights*
• *<https://docs.google.com/spreadsheets/d/1EEuC9sI1BfrKxRPv6kGp0rcw9OxCThhxAGMRBuJga3I/edit?gid=198305328#gid=198305328|28% lift>* in SMS purchase rate for paid users sending emails
• *<https://docs.google.com/spreadsheets/d/1EEuC9sI1BfrKxRPv6kGp0rcw9OxCThhxAGMRBuJga3I/edit?gid=198305328#gid=198305328|5% lift >*in SMS Send Rate for paid users sending emails
• <https://docs.google.com/spreadsheets/d/1EEuC9sI1BfrKxRPv6kGp0rcw9OxCThhxAGMRBuJga3I/edit?gid=198305328#gid=198305328|54% lift >in recommendation take rate (static vs our variant)
• *Blistering 5 weeks* from idea :arrows_right: shipped
:boom: *Business Impact*
• FY26 / FY27 revenue impact: <https://docs.google.com/spreadsheets/d/17_AbHz49qPcFVItku8_TZXpDb7CJtWivoGuTh-jZIqQ/edit?gid=581828261#gid=581828261|$148K / $588K>
• Contributes <https://docs.google.com/spreadsheets/d/17_AbHz49qPcFVItku8_TZXpDb7CJtWivoGuTh-jZIqQ/edit?gid=581828261#gid=581828261|7 bps> toward FY’26 SMS penetration rate target of 4.2% (now 3.11%)
• Defined a working model for bringing differentiated AI to market across our product teams
:question:*What’s next*
• Applying this model for releasing AI to other Mailchimp teams
• Improving the number of support email topics for generation
• Iterating on the current funnel (crafting a draft campaign, multiple options, feedback loops)
• Expanding this to new entry points like Omnichannel templates
:extreme-teamwork:  A very sincere and heart felt thank you to those who just brought our scaled AI+Omnichannel future closer into view: *MLE:* <@U076X3M3KB7|Mike Belov> <@U075K51T3KJ|Jake Headings> <@U02KZLGL3FT|Alex Perez> *AI Science:* <@U02KMAA382W|Hima Polimetla> <@U0793KXBF51|Bryan Smith> *Engineering (Email team):* <@U06GTAA3E8G|Justin Little> <@U02K6LEHGKZ|JB Lovell>  *DS:* <@U03BZL23C1F|Heuisu Kim><@U0970UUFN80|Ashish Prakash> <@U091QJQCRMZ|Yiwen Yan> *Design:* <@U02KM1TUH8B|Ashley Lawrence> <@U02KJF76MU5|Rujuta Apte> <@U03MENW19HA|Isabella Scheier> <@U02KZMX4E6M|Celeste Mora (they/them)> *Engineering (Growth):* <@U09LGAM2PHT|Arpit Parekh>  <@U098480GM26|Minal Rivonker> <@U02KMCXQJ7M|Kelly Hale> *Leadership:* <@W8FHXCZSP|Saikat Mukherjee> <@U07AX5J7MFB|Eric Anderson> <@U02K6NWDM7H|Marlene Mayfield> <@U02KJEHK677|Neil Desai>  TPM: <@U0725TR032M|Katherine Powell> <@U076PQ83WPJ|Ana Bell>  GTM: <@U096X02TTP0|Kendall Kautz>  Legal: <@U04FF36UREJ|Lina Lozano Oviedo>  *Product:* <@U085FK1578R|Bilel Bouraoui> & <@U02KPE15PCL|Connor Callahan>
Thread: 5 replies (latest: 2026-02-11 13:44:37 PST)
Reactions: tada (26), clap::skin-tone-3 (4), clap (8), letsgoooo (8), rocket (7), celebrate-6254 (8), clap::skin-tone-5 (2), clap::skin-tone-2 (3), clap::skin-tone-4 (2), raised_hands (1)



---

=== Message from Margarita Caraballo (U02KJDT7YMT) at 2026-02-06 11:51:29 PST === 
Message TS: 1770407489.403539
:id: :rocket: *Launched  |  Mailchimp Login Cookie Improvements*

For a while, Mailchimp users have been confused about how engagement with the “Keep me logged in” and “Skip for 30 days” features for login worked and how to ensure they were properly enabled. Taking action on some direct user concerns, the new Mailchimp Identity Experience team, who joined the Identity space in December, have taken great steps to analyze customer concerns from VOC and care teams alike, generating some great results for our customers.

With several releases since they joined, we are meeting our customers in the way they expect us to. Because a good identity system works best when we finely balance security, privacy, and reduced friction experiences. By making sure we’re there when they need us, but reducing our presence when they don’t.

:sparkles: *Highlights*
• *46%* :chart_with_upwards_trend_intensifies: *increase in redirects past login this month (such smooth login!)*
• 65% :chart_with_downwards_trend: down-turn in negative VOC through qualtrix and other sources
• Reduced average daily session relogin from 2x to <1.5
• Reduced SMS related self-lockouts due to excessive code requests
:arm-wrestle-high-handshake-business: *Impact*
• Positioning our existing users to get into the product and their tasks more quickly
• Eliminating negative CSAT impacting our brand image
• Modernizing our capabilities to be more frictionless while maintaining security and privacy
:question:*What’s next*
• We’re going to be running an experiment in applicable regions to enable “Keep me logged in” by default
• We’re digging our teeth into performance improvements we can make to our signup and login infrastructure
• Partnering with our VOC team to pilot proactive trend alerting so we can consume and act on user feedback more quickly and avoid an accumulation of negative customer sentiment.
:salute-cat: A big thank you to the core team <@U02KMAX8QUT|Jason Veatch> <@U02KPENAJ0L|Chris Whyte> <@U02LZSZN9J8|Samuel Barksdale> <@U063CC72YRX|Haley Barlar> <@U03CH434152|Varun Murthy> and to our leads who helped them onboard so fast they kicked butt quickly <@U02KEQF9LVC|Ticean Bennett> <@W8FHX8G9Z|Bimal Manukonda> <@W8FQB94DB|Ravi Channapati> <@W8F4XD9U1|Arun Avanathan> <@W8GN4BUBH|Danh Dang> <@U06QRS4SEBC|Rianna Schanno> <@U06K8UTTSJE|Jing Wang> our cross-functional partners <@U02KM9USVDY|Greg Clark> <@U03A5T1UH4M|Matthew Hendler> our partners in acquisition funnel excellence <@U02KPL46GDS|Munia Rahman> <@U02KMH6M4PM|Wes Hall> <@U05UH8ZM6N9|Maddie Jones> <@U02URC9KK46|Lawrence Ma> our buddies in VOC who helped surface this, but more importantly are helping me make sure we’re proactive and not reactive <@U02K6PV38NT|Rob Adair> <@U02L03X7BFB|Rachel Dagley> and our legal and privacy partners <@U08PARER3G8|Sherrie Schiavetti> and <@U035ZCH9U9X|Charles Jin>
Thread: 6 replies (latest: 2026-02-08 16:52:04 PST)
Reactions: oooooo (19), mushroom_celebration (8), niceeee (10), extremeteamwork (8), clapclap (10), rocket (7)



---

=== Message from Connor Callahan (U02KPE15PCL) at 2026-02-09 09:48:41 PST === 
Message TS: 1770659321.318749
:trophy: :europe: *Launched | Mailchimp SMS now covers more of Europe than Klaviyo + Attentive (25 new countries)* :rocket:

For 17% of our paid customers and via our sales teams, the feedback has been consistent: "I can’t adding SMS to our marketing strategy, because it isn’t available in our country." *Based on your feedback, we* *tripled* SMS from *12* :arrows_right: *37* countries and territories globally. *Including 34 in Europe (out pacing Klaviyo and Attentive).* 

:boom:*Impact*
• :sms: 83% :green-arrow-right-filled: *89%* of Mailchimp paid users can *Purchase SMS*
• :money-in: These markets represent a *+7.3 % increase* in the number of paid Mailchimp users who can purchase SMS
• :trophy: *First major competitive differentiator for MC SMS:* *"*Mailchimp SMS is available in more of Europe than Klaviyo and Attentive combined"
• SMS long numbers now available in *Belgium*:belgium: 
• SMS branded senders now available in *the Nordics* :flag-no::flag-se::flag-fi::flag-dk::flag-is:  and *<https://docs.google.com/spreadsheets/d/1gratjN0jRode2g9UdaLiHWid-ThJ3dPwNwHgeX5uG9w/edit?gid=1088572406#gid=1088572406|20 other European markets>*
*What’s next?*
• *New channels:* Building toward RCS :rcs: & WhatsApp :whatsapp: so customers can engage their contacts with rich messaging
• *New sender types:* We’ll continue expanding sender options across markets (alpha in Australia & the UK, Toll-free in the US, Short Codes in New Zealand) with the goal of giving customers more flexibility in how they show up in the inbox.
:extreme-teamwork: *Dreamwork Merits Celebration*
 A major thank you to everyone who designed, built, tested, reviewed, and helped land this with quality: Messaging, Audience, Segmentation, Forms, PLC, Reporting & Analytics, Automations, OBX, Web, Web Ops, QA, FARM, GTM, DS, Technical Content, Billing, FDTG, Revenue Recognition, MSE and Legal: <@U076PQ83WPJ|Ana Bell> <@U02KMCPHWAX|Laura Celentano> <@U02KM87A7SN|Brittany Tims> <@U037ZE99WC9|Madaline Goldstein> <@U07T1UYE259|Rick Barker> <@U09M523DGN8|Kartey Hingu> <@U04V3NDEVC2|Krishna Desai> <@WAD43M6QK|Venugopal Kothuri> <@U09LGAN8CKF|Raji Golla> <@U09L9CPSPV4|Steven Vachon> <@U0703THQZRQ|Gary Aloisio> <@U094R1RP1D5|Charles Hall> <@U094R1RP1D5|Charles Hall> <@U09T9KXDXFY|Uday Srinivas Medisetty> <@U03BZ61PHTK|Ryan Tay> <@U07LPMM9HL6|Chintan Patel> <@U02LANRD7R6|Adam vanWestrienen> <@U05UYGBTQ3T|Nikki Panda> <@U07MMCUPASK|Leah Criscolo (they/them)><@U03LTUC0RA8|Abhishek Salve> <@U06N722QGP3|Anila Mada> <@U09GBP7QP32|Fernando Rodriguez> <@U09FE7Q8GRZ|Ivan Navarrete> <@U04G5KNNVUM|Katie Witkowski><@U0776PKRVP1|Brittany Morrow><@U03UPFR5PB5|Sarah Mullins><@U060NKPDHF1|Swati Bala Subramanian><@U05LMA1PUCR|Miriam John> <@U07F2TB4Q1K|Sunali Bhandula><@U02K6LD7X71|Jocelyn Hardy><@U06D0QM9L1F|James Dominic> <@U06T2RV3755|Jyothi Karlapudi> <@U09SQ2QK3CG|Kalio OFarril> <@U03BN5DCNMT|Ruth Libowsky> <@U06DNT6E69F|Swanand Patil> <@U02KJ9AN5FF|Christian Blades> <@W0133SBDGCA|Chung (Chunghee) Kim> <@U0996V08PQB|Krishna Gudimetta> <@U07161A8XDW|Artur Tarasenko> <@U03TDLSFYH0|Ben Marks> <@U09PS80BY85|Mesam Haider> <@U09MSSM0GP3|Pascal Audant> <@U04QZ1RRPLN|Ty Kuhn> <@U03J3GGU5T3|Jeremey Nofzinger><@U02KJF76MU5|Rujuta Apte> <@U03V70QRTRQ|Mythili Gopikanth> <@W8FQBKGUD|Dustin Yu><@W013E2DDP3J|Alina Rainsford> <@U07NM1TFPAB|Zach><@U07USKD0MA5|Shefali Dalal> <@W012EU6L7FG|Payton Camilli> <@U02KEJS1A3Y|Jay Sun> <@U07TBG84162|Andres Botero> <@U05KZB08WRY|Jon Griffin> <@U035AGFSBRC|Sabrina Harris> <@W019Y5V05UG|Mohammad Habbab><@U02K6SAGNUX|Zack Wright> <@U02KME26NUB|Michael Pazinets> <@U07996KNNPM|Evangelos Rigopoulos> <@U0792LBEUFQ|Christoforos Boukouvalas><@U06QZKUP142|Sean Fleming><@U02KZSQSXAM|Curt Shearer> <@U045QK7AM1A|Anesia Smith> <@U07MYEG53JB|Rhomaro Tesfai-Powell><@U02KEHK13FG|Daniel Varela> <@U02KMDEB5GS|Llewellyn Berg> <@U02KJAPC277|Glenn Branscomb><@U06QWR7FV9T|Elizabeth Bertasi> <@U02KMC0QGSW|Justin E. Samuels><@U02LARVGVGQ|Amanda Hunt> <@U02KPJ7A6UC|Karen Shea><@U032WKWKF2P|Harshada Desai><@U033P0AEQ5A|Zach Hall><@WP0ENL12Q|Deepak Mirani> <@U081SRZEGUE|Andy Nguyen> <@U092PTWA2V9|Ramon Ramirez><@U06QRS4SEBC|Rianna Schanno> <@U03AME5740K|Chima Okechukwu> <@U07R0TLDJ4E|Naga Pradeep Gajula>, <@U03C6DP87PF|Mostafa Derakhshan> <@U06PSKLD0F5|Anastasia Arnold> <@U02KZTXSPTK|Erica Jones><@U096X02TTP0|Kendall Kautz> <@U096DLJK8NA|Jonathan Rodgers> <@U02KEQJS3LN|Wade Burrell> <@U07H0CAQVNH|Giulia Salatino> <@U094GCV941F|James Panter> <@W8FMAUCN8|Ambrose Fung><@U033CC0AUD8|Caroline Josey> <@U02LARVGVGQ|Amanda Hunt><@U06UQL9V07R|Himanshu Dubey> <@U02724E1DFB|Jeremy Diaz> <@U0970UUFN80|Ashish Prakash><@U098R1R6E2U|Lakita Backum> <@U02KPDF0CSY|Cheryl McCurdy> <@U02K6FQMGRM|Cody Sanders> <@U02K6K3VC2K|Emily Roberson> <@U02KM86R9RQ|Cornelius Jones><@W8FHXCZSP|Saikat Mukherjee> <@U07AX5J7MFB|Eric Anderson><@U02L0465FU1|Tara Sharp> <@U07Q0RN0C5S|Renee Moore> <@W8FMB5WKW|Barb Magner> <@U05QNVD0KHP|Cuc Le> <@U04FF36UREJ|Lina Lozano Oviedo> <@U02KJEHK677|Neil Desai> <@U02KPE15PCL|Connor Callahan>
Thread: 7 replies (latest: 2026-02-10 13:48:49 PST)
Reactions: raised_hands (39), sweden (12), tada (30), iceland (8), clapclap (20), rocket (23), raised_hands::skin-tone-3 (6), raised_hands::skin-tone-4 (6), raised_hands::skin-tone-2 (9), partyparrot (11), party_blob (14), party-gritty (6), clapping-all (6), eyes (4), trophy (5), raised_hands::skin-tone-5 (1), gojo-dancing (4), euflag (4), eurocup (3), teamwork-high-five (4)



---

=== Message from Bilel Bouraoui (U085FK1578R) at 2026-02-10 09:26:11 PST === 
Message TS: 1770744371.427739
:robot_face::trophy:   *Launching Email AI Sections* 

37% of marketers say lack of time is their biggest obstacle to building more sophisticated campaigns and reaching better outcomes. For *content marketers and newsletter senders,* emails already average 6.5 sections, making creation slow and manual.

Following the launch of ChatGPT and SMS Campaign Recommendations with our SMS partners, the Agentic team—partnering with the Email team—has launched AI Sections.

AI Sections help marketers generate email content instantly by providing context via URLs or text, dramatically reducing time to launch high-quality campaigns.

*Early Sign of PMF* 
• Emails created with AI and sent have up to 11 sections [<https://us17.campaign-archive.com/?u=c53ae018597741039cfc1078a&id=4385bdeec5|sample> of an email sent]
• :page_with_curl:1.6 AI-generated sections per campaign on average
• :grinning: <https://docs.google.com/spreadsheets/d/1C0vzNrS9Xd6zU_B1GgRV4sohICJJOqhxp-SOsbmqPRQ/edit?usp=sharing|43.7> % of users adopted the feature after trying it
• :grin:<https://app.amplitude.com/analytics/intuit-portfolio/chart/ipk28irx?sharingId=L8nDMsvx&source=copy+url|30.1%> used the feature more than once in a week 
• :star-struck:<https://app.amplitude.com/analytics/intuit-portfolio/chart/ipk28irx?sharingId=L8nDMsvx&source=copy+url|19.7%> of users used the feature 3+ times in a week

*What’s Next*
• Power Campaign Recommendations using AI Sections
• Deeply embed AI Sections into NUNI editor workflows, ChatGPT, and  our flagship AI initiative, Freddie AI, to drive adoption. Current adoption is 3.5%, compared to 1.4% for AI Images and 7% for pre-built layouts.
*Why It Matters: a win after many years of trying!* 
Large-scale initiatives like RevIntel and Marketing Agent v1 were blocked by the inability to generate on-brand content. This is the first time we’ve solved the core problems in content generation—writing style, brand voice, contextual understanding, and layout generation.

*Team* 
Eng: <mailto:justin_little@intuit.com|Justin Little> <mailto:neil_bancherosmith@intuit.com|Neil Banchero-Smith> <mailto:sanquan_prioleau@intuit.com|San'Quan Prioleau> <mailto:ryan_tay@intuit.com|Ryan Tay> <mailto:jb_lovell@intuit.com|JB Lovell>
Data Eng: <mailto:baris_dundar@intuit.com|Baris Dundar> <mailto:erin_elsbernd@intuit.com|Erin Elsbernd>
DS: <mailto:heuisu_kim@intuit.com|Heuisu Kim> <mailto:yiwen_yan@intuit.com|Yiwen Yan>
Design: <mailto:isabella_scheier@intuit.com|Isabella Scheier> <mailto:celeste_mora@intuit.com|Celeste Mora>
Eng Leaders: <mailto:eric_anderson1@intuit.com|Eric Anderson> <mailto:inderbir_pall@intuit.com|Inderbir Pall> <mailto:marlene_mayfield@intuit.com|Marlene Mayfield>
PM: <mailto:ose_amiegheme@intuit.com|Ose Amiegheme> <mailto:bilel_bouraoui@intuit.com|Bilel Bouraoui>
PM / Design leaders: <mailto:andrew_firstenberger@intuit.com|Andrew Firstenberger> <mailto:nathan_snell@intuit.com|Nathan Snell>
TPM: <mailto:katherine_powell@intuit.com|Katherine Powell>
GTM: <mailto:nina_zhang@intuit.com|Nina Zhang> <mailto:katie_witkowski@intuit.com|Katie Witkowski>
QA: <mailto:essence_coleman@intuit.com|Essence Coleman>
UXR: <@U02KEAWH2KY|Alex Dao> 
Thread: 1 replies (latest: 2026-02-10 16:11:37 PST)
Reactions: amazing45 (17), celebrate (11), rocket (10), ai-intensifies (6), raised_hands (2), peanutbutterjellytime (1)



---

=== Message from Louis Pan (U095D83P9UN) at 2026-02-10 11:07:15 PST === 
Message TS: 1770750435.194979
:rocket: :funnel: *Launched* *the* *Shopify New Customer Funnel Experience* 

*Problem*
We were losing 3,199 Shopify users per month in the connection funnel where we saw only 33% of new customers that install the app end up selecting a plan and landing in the product.

*What we shipped*
With this release, we *made it simpler for customers to signup and get started with the product* by shipped a revamped experience for new customers with:
• Fewer steps (~11 → 5 screens) 
• Pre-filled forms, 
• Automatic data sync start for new accounts
*Experiment Results*
We shipped this experience as a 50/50 experiment to compare the performance of the new vs. legacy new customer funnel. The results show the *new funnel experience is a clear winner,* where we’re seeing:
1. *More customers are completing the funnel:* +7% more customers complete the funnel and get into the product after install. (Complete funnel rate from 33% → 40%)  
2. *More customers are connected and active:* +6% increase in customers with active store synced (90% → 96%) 
3. *More <https://docs.google.com/presentation/d/1QeiIxhFi93t1uMqkojfh-Og7NbufPMGgSHtHX2H6qz8/edit?slide=id.g3bb867b25e0_13_10#slide=id.g3bb867b25e0_13_10|healthy customers syncing data> that will retain*: +5% customers with contacts OR products synced (90% → 95%) 
*Business impact*
We expect these results to drive acquisition of ~4,400 additional active users per year with 4,000 new free tier users and 400 Standard plan users.

*What's next*
In Q3, there are plans across integrations to build upon these improvements to further improve the integration lifecycle management to make connection even more seamless as well as post-connection experiences to reduce time-to-payoff and value for these customers.

*Acknowledgements*
This took a village and wanted to pause and say a sincere thank you to everyone who designed, built, tested, and shipped this experience and brought us closer to a friction-free path for Shopify merchants.
• Team: <@U035CBMRTND|Nathan Leggatt> <@U06MWRJ6EQ4|Mary E Ellis> <@U07PQDS6F62|Josh Lynch> <@U085DCH3MCN|Josh Bernhard> <@U04D7TX5LDB|Ryan Hungate> <@U04DDAJFF6G|Jordan Rich> <@U07J4NHVCBU|Kyle Johnson> <@U04E0GY4D96|Kyle Hungate> <@U02KMBTRKL2|Jenna Fitzpatrick> <@U02KJ9QRSDT|Eddie Shrake> <@U03DJNFKW4T|Nicole Robinson> <@U02KJFNSB6H|Philip Allen> <@U08DYEMBSSG|Jason Cross><@U02KEHAB5U6|Claudia Majors> <@U06THT1TTRN|Viren Sharma> <@U02KPGZ4HHS|Jane Guthrie> 
• Leadership support: <@U08KK7S6LAZ|Diana Williams> <@W8FHYGK19|Jack Tam> <@W8FQBMAN9|Andrew Firstenberger> <@W8F0RNH4Y|Nathan Bullock> <@U09QF7F45AQ|Nathan Snell> <@W8FHXCZSP|Saikat Mukherjee> 
*Resources:*
• <#C09SM7DKZ2T|shopify-new-customer-funnel>
• <https://drive.google.com/file/d/1B3DVbWKBtbA5NIurQNTow_OppiQvYnnN/view?usp=drive_link|Demo Video - New Funnel>
• <https://drive.google.com/file/d/1NXwES72vfaAMmooUThqHPjMkfXNT3CXl/view?usp=drive_link|Demo Video - Old funnel>
• <https://www.figma.com/design/98XkBqTdwwmbLDvnInmpmm/Integrations-Connection-Funnels?node-id=762-8459&t=dtWoDBBo5s6SFmBA-1|Figma>
Thread: 2 replies (latest: 2026-02-10 16:30:22 PST)
Reactions: lets_go (15), heart_hands (4), heart_hands::skin-tone-2 (1), rocket (8), raised_hands (3), raised_hands::skin-tone-2 (1)
Files: FTU Funnel - Current.mov (ID: F0A7J3J9P7E, video/quicktime, 85.3 KB), 23 - DSB (ID: F0AADKN41QA, application/vnd.google-apps.presentation, 0 Bytes), FTU Funnel - New.mov (ID: F0A7CET23C6, video/quicktime, 107.2 KB)



---

=== Message from Nick Triscritti (U09A9P01S4F) at 2026-02-10 13:23:32 PST === 
Message TS: 1770758612.033649
*Launched* :rocket: *| Mailchimp Pixel - First-party site tracking for Shopify, Wix, and WooCommerce*

*Problem* :bulb:
Small business marketers using Mailchimp struggle with activating timely, behavior-driven campaigns because our current mc.js / Connected Sites implementation is unreliable, hard to verify, and doesn’t deliver the real-time signals they need. Customers have been asking for this, and it brings us closer to parity with competitors. With this release, we’re meeting them where it hurts: we’re introducing a first-party Mailchimp Pixel (SDK + ingestion + processing) so website behavior becomes a first-class, dependable signal in Mailchimp.

*What we launched* :dart:
• *Pixel management experience* - Turn Pixel on / off, copy install snippet, and view status in the integration settings (Shopify, Wix, WooCommerce).
• *Automations + Segmentation* - Existing behavior-based triggers (Views Page, Views Product, Adds to Cart, Checkout, etc.) and segmentation conditions now work for Wix and WooCommerce (requires C1 eng trigger setup) in addition to Shopify, so all pixel-enabled stores can use the same journeys and segments.
*Why it matters* :sparkles:
• *Reliable behavior signal* - First-party pixel reduces failed or delayed event capture and improves the accuracy of data flowing into segmentation and automations.
• *Competitive parity* - Where Klaviyo's pixel currently wins, we now have a comparable, first-party story.
• *One behavioral layer* - One pixel and event model across Shopify, Wix, and WooCommerce so we can build and support a single set of features instead of platform-specific workarounds.
*Business impact* :check-circle:
We expect this to unlock behavior-driven automations and segments for Wix and WooCommerce stores that previously had no reliable first-party behavior signal, and to improve connection verification so more merchants can confidently turn on Pixel.

*Who's impacted* :busts_in_silhouette:
All Mailchimp Ecommerce users with Shopify, Wix, or WooCommerce integrations.

*What changed (before / after)* :arrow_left: :arrow_right:
• *Before:* Behavior triggers (Views Page, Views Product, Adds to Cart, Checkout, etc.) and S2S segmentation conditions were available only for Shopify (or Blotout). Abandoned Browse was Shopify-only.
• *After:* Same triggers and conditions are available for Wix and WooCommerce (and any future pixel-enabled integration), including abandoned cart.
*What's next* :soon:
• Wix & WooCommerce 1-click install of the pixel (end-Q3).
• Additional ecomm platform support and custom / auto-event capture (Q4+).
*Thank you* :tada: :raised_hands: 
As we all know, this is no small undertaking and it wouldn't be possible without everyone's diligent support. Thank you to all who designed, built, tested, and shipped this and gave our C1s a reliable path to behavior-driven campaigns. Apologies if I missed anyone.

• *Team:* <@U07U1NNUHRC|JP McConnell> <@U079Y3PKJLQ|Vassilis Dourdounis> <@U02KEEED9LN|Amit Khare> <@U07996KN0V9|Thodoris Batsikas> <@U035CBMRTND|Nathan Leggatt> <@U06MWRJ6EQ4|Mary E Ellis> <@U085DCH3MCN|Josh Bernhard> <@U04D7TX5LDB|Ryan Hungate> <@U03DJNFKW4T|Nicole Robinson> <@U02KEQP5A6S|Wei Jia> <@U05DQHZTQ3T|Jane Krause> <@U02KJ9QRSDT|Eddie Shrake> <@U02KJFNSB6H|Philip Allen> <@U08DYEMBSSG|Jason Cross> <@U02KEHAB5U6|Claudia Majors> <@U02KPGZ4HHS|Jane Guthrie> <@U079SMT5UTA|Matt Cimino> <@U086MMX7W0M|Juliana Simoes> <@U02K6PULZQX|Pooja Berrong> <@U07PJK7TTPE|Brooke Addison> <@U03R9TTF7FY|Abby Barnett> <@U02K6FQMGRM|Cody Sanders> <@U02KJDA2QSH|Maegan King> <@U02KENZHH6J|Robyn Taylor> <@U04G5KNNVUM|Katie Witkowski> <@U02L0465FU1|Tara Sharp> <@U07Q0RN0C5S|Renee Moore> <@U06QWR7FV9T|Elizabeth Bertasi> <@U02KMGM5D98|Yena Ku (they-them)> <@U02KMAW39GB|Gauri Nagpal Chang> <@U03KUBTCSG1|Frank Persico> <@U02P9STSQGZ|Becca Walsh> <@U07UCSZSA30|Keith Ferney> <@U02KJBP43V3|Jess Riddle (She/Her)> <@U07Q70L7BC5|Vova (Vladimir) Shechtman> <@U02KJE3FRFX|Michael Plattner> <@U07B96L9T9N|Adam Mitchell> <@U07PNSRLYR5|Tommy Miller> <@U07FRV7RNJX|Tao Zhang> <@U02KM7L9D7U|Colt Carder> <@U03TDGU2JUB|Josh Day> <@U09BAMA1N9X|Nakul Lahoti> <@U09AYBGMDV1|Arpit Tyagi>
• *Leadership support:* <@U08KK7S6LAZ|Diana Williams> <@W8FHYGK19|Jack Tam> <@W8FQBMAN9|Andrew Firstenberger> <@W8F0RNH4Y|Nathan Bullock> <@U09QF7F45AQ|Nathan Snell> <@W8FHXCZSP|Saikat Mukherjee>
*Resources* :books:
<https://www.figma.com/design/oc3MCMIdKOdNTnERkv8PrU/Pixel---FY26?node-id=289-42026&p=f&t=nSoqGWDV30qX9lbp-0|Figma> · <https://docs.google.com/document/d/1oDiGa34f70lGmhiqizcjmSwqeGk6P-0keaY8rNxsFUo/edit?tab=t.tuana7w8az7b|PRD> · <https://mailchimp.com/help/about-mailchimp-site-tracking-pixel/|KB>
Thread: 10 replies (latest: 2026-02-11 06:02:24 PST)
Reactions: vibecat (19), awyeah (10), pixel_heart (14), raised_hands (12), raised_hands::skin-tone-2 (2), raised_hands::skin-tone-3 (2), awesome-star (3), rocket (8), dancingdino-3573 (4), dancing-blob (5), raised_hands::skin-tone-4 (1)
Files: DRAFT - FY26 Pixel PRD - NCT (ID: F09J6LQDDCK, application/vnd.google-apps.document, 0 Bytes)



---

=== Message from Elizabeth Bertasi (U06QWR7FV9T) at 2026-02-10 13:39:06 PST === 
Message TS: 1770759546.231899
:rocket: :cjb: :new: *New “Back in Stock” experience launched!*

:search-pin: *What’s new?* 
*MANY* teams have partnered to launch a new "Back in Stock" experience that enables C1s to collect interest in out of stock products and automatically notify users who have signed up for back in stock alerts when the product is available again.
*In-Page Out-of-Stock Opt-In*
    ◦ A "Notify Me When Available" button on out-of-stock product pages.
    ◦ Clicking the button opens an opt-in form (email/SMS capture).
    ◦ Interest is saved to the customer’s C2 profile in Mailchimp.
*Automated Customer Interest Capture & Management*
    ◦ Customers who opt-in are stored in a "Back-in-Stock Queue."
    ◦ Ability for C1s to see which products customers are waiting for.
*Triggered Back-in-Stock Automation*
    ◦ When a product is restocked, an automation is triggered to notify all customers who opted in.
    ◦ Ability to exclude certain products from triggering notifications.
*Dynamic Email & SMS Notifications*
    ◦ One-time setup for back-in-stock notifications.
    ◦ Uses merge fields to dynamically pull product name, image, price, and link.
    ◦ Covers all SKUs instead of requiring separate setups for each product.
    ◦ Optional ability to customize product-specific messages.
*Scalability & Competitive Advantage*
    ◦ A *dynamic setup* that scales across a brand’s entire catalog.
    ◦ Advanced filtering options to refine notifications (e.g., exclude low-stock products, prioritize high-demand items).
    ◦ Visibility into *who is waiting for what*.
:analytics-graph: *Impact & metrics:*
• In our experiment, we saw 17 users publish a back in stock form. 7 users turned on a back in stock automation. This experience has been converted to a back test, so we’ll continue to measure impact over time as adoption and results accumulate. 
• <https://app.amplitude.com/analytics/intuit-portfolio/dashboard/lbc52vk4|Automations trigger expansion Amplitude dashboard>
• <https://app.amplitude.com/analytics/intuit-portfolio/dashboard/9ok9343f|Forms Amplitude dashboard>
:coming-soon-icon: *What's next?* 
We’ll get laser-focused on increasing adoption of these features so our users can see real value, we’ll measure C1 business impact for those adopting these features, and we’ll work on expanding this capability to additional ecommerce platforms.

:clap: :clap: *Shout outs -* this was a *huge* effort by so many folks, so give these peeps a high five the next time you see them in the office (and if I have missed any names please let me know so I can add!):
Automations: <@U09BAMA1N9X|Nakul Lahoti> <@U03GVFDGUKA|Cliff Martin> <@U02KMGM5D98|Yena Ku (they-them)> <@U02KJ1UDHC5|Bobby Craig> <@U03GE2Y59M0|Dana Winn (Automations Oncall)> <@U02KZU660AV|Jameson Brown> <@U02KMC0QGSW|Justin E. Samuels> <@U07UCSZSA30|Keith Ferney> <@U02KMDU1TU2|Maxwell Reich> <@U07NA0QPYJ0|Saisharath Peddibotla> <@U02P9STSQGZ|Becca Walsh> <@U02KZMX4E6M|Celeste Mora (they/them)> <@U02KMBDS7AP|Heather Dartz>  <@U06QRS4SEBC|Rianna Schanno> <@U02KJBP43V3|Jess Riddle (She/Her)> <@U02KJ5X1V3P|Cary Duncan> <@U086MMX7W0M|Juliana Simoes> <@U02R5B0HN4F|Vlad Khvan>
Forms: <@U07996KNNPM|Evangelos Rigopoulos> <@U0792LBEUFQ|Christoforos Boukouvalas> <@U071LK28822|Chris Chung> <@U02KMA7JMPV|Dev Sabharwal> <@U06K1M3KGHZ|Laura Guillen> <@U02KMCXDD27|Katie Eldredge> <@U02K6SAGNUX|Zack Wright> <@U079SMT5UTA|Matt Cimino>
Integrations: <@U02KJFNSB6H|Philip Allen>, <@U02KM2QGKEW|Ali Heidary>, <@U09E6FWDJSK|Vahid> <@U09U6117EG0|Martin Madiri>, <@U02KMBTRKL2|Jenna Fitzpatrick>, <@U02KPGZ4HHS|Jane Guthrie>, <@U095D83P9UN|Louis Pan> <@U04D7TX5LDB|Ryan Hungate>, <@U07J4NHVCBU|Kyle Johnson>, <@U04DDAJFF6G|Jordan Rich> <@U07PQDS6F62|Josh Lynch>, <@U03R9TTF7FY|Abby Barnett>, <@U07PJK7TTPE|Brooke Addison> <@U079Y3PKJLQ|Vassilis Dourdounis>
Audience: <@U03FZ581XTR|George Nakkas> <@U05LRND7CPN|Nikhil Monga> <@U035AGFSBRC|Sabrina Harris> <@U07USKD0MA5|Shefali Dalal> <@U050GEXLRV3|Alberto Santos> <@U02K6JTS4H5|Eddie Ornelas> <@U030ALNTZTR|Isaac Melton> <@U02KZL81PLH|Caroline Ramirez>
CDP: <@U04NGRG0RH9|Lauren Colwell> <@U07GRQTTY30|Arkesh Rath> <@U07146FU35X|Jeffrey Li> <@U04SC218QQ3|Sijia Liu> <@U078B7PT3A8|Dan Damkoehler>
Segmentation: <@W019Y5V05UG|Mohammad Habbab> <@U07Q70L7BC5|Vova (Vladimir) Shechtman> <@U05KZB08WRY|Jon Griffin> <@U04TFSEP31D|James Sheridan> <@U072QE8MQ05|Jessica Rocha> <@U04TWCYUZAN|Mason Hadeler> <@U07HS0D491P|Antony Joyson> <@U09KX2AHX35|Kannan arumugam> <@U07TY6D8Z0F|Brandon Culp> <@U07S0HEP5T9|Jared Malcolm> <@U0A6Q4HJDU2|Vishal Varak> <@U035AGFSBRC|Sabrina Harris> <@U07USKD0MA5|Shefali Dalal> <@U03KUBTCSG1|Frank Persico>
Email: <@U02K6LEHGKZ|JB Lovell> <@U04SYBP56JZ|Michelle Ducote> <@U03TC2MB06M|James Arama>
SMS: <@U03NU55364D|Satish Sambandham> <@U0946BZ3QTW|Mike O'Dell> <@U03V70QRTRQ|Mythili Gopikanth> <@U04QZ1RRPLN|Ty Kuhn>

 <@U08KK7S6LAZ|Diana Williams> <@U07AX5J7MFB|Eric Anderson> <@W8FHXCZSP|Saikat Mukherjee> <@W8FHYGK19|Jack Tam> <@W8FQBMAN9|Andrew Firstenberger>
Thread: 4 replies (latest: 2026-02-10 16:29:34 PST)
Reactions: cat-rave (34), raised_hands (16), fire (19), rocket (21), raised_hands::skin-tone-3 (6), raised_hands::skin-tone-4 (2), clapclap (7), raised_hands::skin-tone-2 (6), shopping_trolley (2), heart_on_fire (1)



---

=== Message from Ofer Frenkel (U06AP1W1284) at 2026-02-11 06:00:07 PST === 
Message TS: 1770818407.696519
:rocket: Launched: Reviews Vertical Integrations (Judge.me & Yotpo)

:warning:  *Problem* 
Until now, product review data has been siloed in third-party platforms. Our e-commerce users had no way to automatically trigger follow-up marketing based on customer sentiment or easily pull their hard-earned social proof into Mailchimp campaigns without manual, technical hurdles.

:sparkles: *What we launched* 
We’ve expanded our ecosystem with first-party, unidirectional integrations for Judge.me and Yotpo, now live in a dedicated “Reviews” category in the Integrations directory. Customers can now:
• *Automated Review Requests:* Trigger emails following a purchase that include a dynamic URL and a featured product image to facilitate review collection.
• *Post-Review Follow-up Journeys:* Deploy automated emails based on the specific star rating submitted, such as sending recovery offers for low scores or upsell messages for high scores.
• *Sentiment-Based Segmentation:* Create and target audience segments using specific review data, including review submission status and numerical star ratings.
• *Enriched Contact Profiles:* Automatically surface granular review events and scores directly within the individual contact’s activity log in Mailchimp.
:dart: *Why it matters* 
• *No-code activation*: Transforms customer experience from manual data synchronization to an automated flow, enabling reviews to function as continuous conversion drivers and brand trust-builders.
• *Competitive Parity:* Closes a top-requested feature gap, matching key capabilities offered by Klaviyo for the ~15% of their base using these platforms.
• *FY26 Growth Lever* - Deepens product stickiness across Shopify and other leading Ecommerce platforms to drive reduction in churn and increase in customer growth.
:busts_in_silhouette: *Who’s impacted*
All Mailchimp Ecommerce users with stores on Shopify, BigCommerce, WooCommerce and Magento.

:construction: *What’s next*
• *Featured Review Content Block* _(Coming 2/23)_: Drag-and-drop block to insert top reviews into email campaigns.
• *Continued ecosystem expansion*: Next focus area: *Loyalty & Rewards* integrations.
*Shoutouts* :raised_hands: They say it takes a village, and this launch was no exception. So many people contributed and worked hard to make this happen across multiple teams - thank you for the incredible cross-functional effort!
(If I missed anyone’s name, please let me know!)

Integrations: <@U02KJFNSB6H|Philip Allen> <@U02KM2QGKEW|Ali Heidary> <@U07U1NNUHRC|JP McConnell> <@U07GARRQRHR|Amar Manjunath> <@U07FRV7RNJX|Tao Zhang> <@U031T5Y29HC|Rohit Mereddy> <@U02KJ9QRSDT|Eddie Shrake> <@U02KPGZ4HHS|Jane Guthrie> <@U07PJK7TTPE|Brooke Addison> <@U03R9TTF7FY|Abby Barnett>
IDX: <@W8F0RAL2U|George Mukkudiyil> <@U06B46M7E5N|Sunita Yadav> <@W8F0RVB4G|Sankar Chidambaram> <@U07QV6A2F8U|Sriram Kalyanaraman> <@W8FL4M81Y|Basil Peter> <@W3X96BZUH|Steve Mendoza> <@U01TCL90T5K|Shashi Yarlagadda> <@U01HJ6ZRH44|Francois Beaussier> <@U06QUDES4NB|Christopher Smith> <@U02S9JC3PC7|Jae Park> <@U01RV4P3NP2|Coleen Ho> <@U038ANPAHGQ|Adrian Sida> <@U07PJK7SZ8C|Saranya Vivekanandan> <@W8FQDKG1K|Uma Maheswari Nagarajan> <@U05077JDW4E|Sujithra Manikandan>
QA: <@U02LB3PKAHW|Matt Castilla> <@U02KZV70EQZ|Jasmine Davis> <@U02KJ5X1V3P|Cary Duncan>
DS: <@U085DCH3MCN|Josh Bernhard> <@U08J8FFFVAL|Stam Paterakis> <@U02KEHAB5U6|Claudia Majors>
Audience: <@U02KZL81PLH|Caroline Ramirez> <@U07USKD0MA5|Shefali Dalal> <@U03FZ581XTR|George Nakkas> <@U02K6JTS4H5|Eddie Ornelas>. <@U050GEXLRV3|Alberto Santos> <@U035AGFSBRC|Sabrina Harris> <@U05LRND7CPN|Nikhil Monga>
CDP: <@U0789R246JY|Leila Jalali> <@U04NGRG0RH9|Lauren Colwell> <@U07GRQTTY30|Arkesh Rath> <@U04SC218QQ3|Sijia Liu>
Segmentation: <@U03KUBTCSG1|Frank Persico> <@U07USKD0MA5|Shefali Dalal> <@U07Q70L7BC5|Vova (Vladimir) Shechtman> <@U05KZB08WRY|Jon Griffin> <@W019Y5V05UG|Mohammad Habbab>
Automations: <@U09BAMA1N9X|Nakul Lahoti> <@U06QWR7FV9T|Elizabeth Bertasi> <@U02KJBP43V3|Jess Riddle (She/Her)> <@U02KJ1UDHC5|Bobby Craig> <@U07UCSZSA30|Keith Ferney> <@U03GVFDGUKA|Cliff Martin> <@U02KZU660AV|Jameson Brown> <@U02KMBDS7AP|Heather Dartz>
Email: <@U02K6LEHGKZ|JB Lovell> <@U04SYBP56JZ|Michelle Ducote> <@U03TC2MB06M|James Arama> <@U09979JPH37|Ose Amiegheme>
SMS: <@U03NU55364D|Satish Sambandham> <@U0946BZ3QTW|Mike O'Dell> <@U03V70QRTRQ|Mythili Gopikanth> <@U04QZ1RRPLN|Ty Kuhn>
Business Development and marketing: <@U05KMGA9QAG|Dani Cook> <@U079XLXJ338|Allie Strack> <@U05FTMF745R|Alexandra Wood> <@U097A9C5YKT|Zane Holt> <@U02R9GEK1F1|Rachel Pimienta>
.Com and WebOps: <@U0517L5N34Y|Avery Felman> <@U02KJ6V3LA1|Cody Solomon> <@U04ALBZD42K|Chris Zeigler> <@U02URC9KK46|Lawrence Ma>
Legal: <@U02K6NH28B1|Lewis Beard> <@U07Q0RN0C5S|Renee Moore>

<@U08KK7S6LAZ|Diana Williams> <@W8FHYGK19|Jack Tam> <@U07AX5J7MFB|Eric Anderson> <@W8FHXCZSP|Saikat Mukherjee> <@U09QF7F45AQ|Nathan Snell> <@U086MMX7W0M|Juliana Simoes> <@U079SMT5UTA|Matt Cimino><@W8FL40142|Prasanna Kumar - (818 312 8772)>
:books: *Resources* 
<https://docs.google.com/presentation/d/1Fks3UtQETKBaZnb8VPut3_FsaDMsZ5pVI8t9cq15qQA/edit?usp=sharing|Yotpo & Judge.Me Integrations Overview>
Thread: 4 replies (latest: 2026-02-11 13:30:10 PST)
Reactions: raised_hands (21), rocket (24), tada (16), fire (16), vibecat (7), raised_hands::skin-tone-2 (5), headbang_ (4), raised_hands::skin-tone-4 (3), raised_hands::skin-tone-3 (4), raised_hands::skin-tone-5 (1)
Files: Reviews Integration Updates: CS Training Session (ID: F0ADX1515HV, application/vnd.google-apps.presentation, 0 Bytes)



---

=== Message from Brittany Reeves (U04DTC9ACLF) at 2026-02-11 10:50:53 PST === 
Message TS: 1770835853.026849
:rocket_launching: *LAUNCHED | Trial Onboarding Cadence* :rocket:

:arrow_right: As part of the larger *self-serve acceleration workstream*, I am thrilled to share that we have launched a new trial onboarding cadence for Standard trial takers in the United States. This new series includes 64:exclamation-red:UNIQUE assets that are personalized for the existing credit card trial experience, as well as versions for the No Credit Card trial experiment and the digital sales ICP.

:blob-question: *Why is this customer-obsessed?* This new series was a huge undertaking on the operational side as it includes a fully responsive journey to the user's behavior with a repository of content. The trial taker will receive 14 potential emails throughout their 14-day trial, guiding them along their journey aligned with in-app optimal business setup actions.

The emails and IPDs are :b01::e01::a01::u01::t01::i01::f01::u01::l02: and even include transactional touchpoints for customers not opted into our marketing comms.

:magnifyingglass: We will be testing this new series against our existing onboarding users for standard users.

This was truly a crossfunctional effort and a huge :mega: shoutout to everyone across ELM, Marketing Ops, Data Eng, Data Ops, Creative, Product, Product Marketing, Analytics, Legal who made this happen. A campaign of this magnitude would normally take months to launch and the team did it in 4.5 weeks. <@U03UPFR5PB5|Sarah Mullins> <@U09B9CFDZC1|Kris Auyeung> <@U0823HP6XMY|Alison Chan> <@U05AL2VAAA2|Mahu Sims> <@W8FL3BQJW|Krysten Dell> <@U07ELKDQ0JJ|Morgan Allen> <@U05A4D12BT8|Alexandra Pappas> <@U06K8UTTSJE|Jing Wang> <@U02K6NWDM7H|Marlene Mayfield> <@U06M322289M|Miles Kim> <@U02RGGQ757U|Laura Adams> <@U02LB4F6R6U|Meg Lindsay> <@U08J3M1RKB2|Rummel Medina> <@U02RL9DEP96|Runwei Wang> <@U04G5KNNVUM|Katie Witkowski> <@U02LARVGVGQ|Amanda Hunt> <@WPV4R19T5|Qingbin (Sonia) Kong> <@U02K6K7S1U7|Elisa Soares> <@U06QRS4SEBC|Rianna Schanno> <@U0A1YPWE9PZ|Levi Montoya> <@U090MFQ1VGB|Sushil Upadhyayula>
Thread: 3 replies (latest: 2026-02-12 14:08:19 PST)
Reactions: yay (14), clapping-all (17), rocket (9), tada (8), celebrate (2)
Files: trialonboarding1.png (ID: F0AED6SAC78, image/png, 149.1 KB), trialonboarding2.png (ID: F0AE8SEGQG3, image/png, 573.3 KB), trialonboarding3.png (ID: F0AEBRETF6Z, image/png, 430.0 KB)



---

=== Message from Amanda Hunt (U02LARVGVGQ) at 2026-02-11 12:21:40 PST === 
Message TS: 1770841300.599669
:clapping-all: *Launched: No Credit Card Required V2 Experiment* :clapping-all: 

:warning:  *Problem* 
There is a large drop-off (68%) between account creation and trial start, and over the past 6 months, this drop-off has increased by 6 ppt. This experiment removes a key friction point in our acquisition to trial start experience – the requirement to provide billing information to start a free trial.

:sparkles: *What we launched* 
This experiment removes the initial billing requirement to start a 14-day free trial of the Standard and Essentials plans and tests the role of product limits within a No CC trial. If a customer provides billing information, they'll unlock the remainder of the free trial email sends and allow Mailchimp to bill them r at the end of the trial period:
• *Variant 1:* No CC Required, Limited to 100 email & automation sends without billing info.  
• *Variant 2:* No CC Required, Backend limit of 10K email sends without billing info
:dart: *Why we have confidence* 
• *From the V1 experiment, we know that removing the credit card gate meaningfully expands top of the funnel and unlocks incremental revenue – though on a delayed curve.* In our No CC V1 experiment, we significantly increased trial starts (+70%) and ultimately drove higher new booking revenue (+6%). However, a majority of that lift materialized after the trial ended, indicating customer evaluation and purchase decisions will extend beyond the trial window. 
• *Our competitors don't require a credit card to start a trial*: Constant Contact, Shopify, Brevo, ActiveCampaign, and Hubspot all have un-gated trials.. 
• *Customers don't expect to provide billing information*: We see a ~60% dropoff at the billing screen during account setup for paid purchase intent customers from dotcom.
:busts_in_silhouette: *Who’s impacted*
All prospective customers and free customers within 90 days in established markets

:pencil2: *Get into the details* 
Check out the EDD <https://docs.google.com/document/d/1M8Vs_XrRaLf-34wWlxAiqFjPFunMgQuJ9JnggAAwU-M/edit?tab=t.0|here>. There's an overview deck <https://docs.google.com/presentation/d/1i7CxRPzbkHV0c9TQnremMSRe5q7B_6bxSG5JcLj_aj8/edit?slide=id.g3baa00a272e_2_1444#slide=id.g3baa00a272e_2_1444|here>. And the Figma is <https://www.figma.com/design/PBlvPE4QXmCqRY1RiYUGwa/No-CC-Required-V2?node-id=16402-189436&p=f&t=dd1fqdK6urQm7RJk-0|here>!

:construction: *What’s next*
Mailchimp’s shift to a no credit card trial doesn’t just change our trial mechanics – it fundamentally changes how we monetize. Revenue is no longer secured via upfront commitment; rather, by how _quickly_ and _effectively_ we can help customers experience and scale real value. You can check out what's next for our trial optimization work <https://docs.google.com/document/d/1q6QbC2DREJyEKnrNJRctH2f01OH_owgK661mAZbJFdQ/edit?tab=t.xbixu5i5ef7q#heading=h.nr7haxcr0p2g|here>.

:shoutout1: *LITERAL DREAM TEAM* :shoutout1:
This experiment required rapid, close collaboration across the business....and y'all, we went from an official kickoff on 1/12/26 to a production experiment by 2/9/26. Here's to the peeps that made it happen across dotcom, PLC, Campaign Checklist, OBX, Automations, Mobile, Marketing, LCM, C1 Communications, Finance, Sales, Legal, Billing, and Customer Care - y'all are the best! <@U07TMNHQ20N|Phuong Trang>, <@U02KM9USVDY|Greg Clark>, <@U02ATLVNQCV|Hrishikesh Babar>, <@U03ETSQ5A1K|Jeremy Tillman>, <@U02URC9KK46|Lawrence Ma>, <@U032WKWKF2P|Harshada Desai>, <@U02KM08JQR0|Aaron Armstrong>, <@U033B9J9GQL|Nicole Newton>, <@U033P0AEQ5A|Zach Hall>, <@U07MYEG53JB|Rhomaro Tesfai-Powell>, <@U02KZSQSXAM|Curt Shearer>, <@U02KEAE3DL6|Bryce Hammond>, <@U05NALW1S3U|Collins Amadi>, <@U047HMUGE82|Erin Szarpa>, <@U07PV9VL1HD|Omar Carrasco>, <@U02K6DM848P|Brendan Tucker>, <@U02KJCMA129|LaTasha Armour>, <@U09B1S1DZ6Y|Sundeep Nadendla>, <@U02KPGQGSVA|Jason Calhoun>, <@W0132PNAC9X|Devin Mercier (he/him)>, <@U02KJBP43V3|Jess Riddle (She/Her)>, <@U02KZMX4E6M|Celeste Mora (they/them)>, <@U06QRS4SEBC|Rianna Schanno>, <@W8GN4BUBH|Danh Dang>, <@U03C6DP87PF|Mostafa Derakhshan>, <@U060RFM8D27|Kranthi>, <@U07R0TLDJ4E|Naga Pradeep Gajula>, <@U06QWR7FV9T|Elizabeth Bertasi>, <@U02KMBDS7AP|Heather Dartz>, <@U09BAMA1N9X|Nakul Lahoti>, <@U02KJ63H57X|Chelsea Youmans>, <@U04HZLGMQCD|Susana C Delgadillo>, <@U02KEM59CCW|Mark Abdelmalak>,  <@U07111XDX1V|Jackson Wearn>, <@U03JKJV4RGR|Marcus Moncayo>, <@U03CJLQEUCF|Remya K> , <@U02KJF2PPUM|Sal Aparo>, <@U08N2BTNV46|Jennie Zhou>, <@U09C3GFP1PU|Minori Jaggia> <@U02LB7D16P2|Vishi Gondi>, <@W01A3N3U6LQ|Arthur Yen>, <@U03RVUX9W7M|Evan Pantels>, <@U02K6K7S1U7|Elisa Soares>, <@U03TDH411GB|Nathan Rambeck>, <@U06LH916YA0|Joey Hurley>, <@U04DTC9ACLF|Brittany Reeves>, <@U03UPFR5PB5|Sarah Mullins>, <@U02RGGQ757U|Laura Adams>, <@U02LB4F6R6U|Meg Lindsay>, <@U0823HP6XMY|Alison Chan>, <@U05AL2VAAA2|Mahu Sims>, <@W8FL3BQJW|Krysten Dell>, <@U05A4D12BT8|Alexandra Pappas>, <@U04G5KNNVUM|Katie Witkowski>, <@WPV4R19T5|Qingbin (Sonia) Kong>, <@U05FNQPLGCW|Ben Ou>, <@U032GEW7U0Y|Brent Hallinger>, <@U07EFT25CBB|Stuart Chuang>, <@U02M49MR0TX|Celia Shore>, <@U02KMFNH082|Scott Cleveland>, <@U02L00GFMEV|Koleen Henson>, <@W8FMB5WKW|Barb Magner>, <@U05QNVD0KHP|Cuc Le>, <@U02LB711L0G|Tyler Ward>, <@U02KJD0UBBP|Laura Thompson>, <@WB6QH3S20|Christine Kuo>, <@W9GLZQ45A|Ryan Tuosto>, <@U0A99U871KR|Sid Bakhru>, <@W8GG7J2RL|Chad Tsang>, <@U0A8293TH9U|Anish Nahar>, <@WERJCJ189|Kyle Spaulding>, <@U06K8UTTSJE|Jing Wang>, <@U02K6NWDM7H|Marlene Mayfield>, <@W8XEU93GS|Cesar Rodriguez>, <@U07AX5J7MFB|Eric Anderson>, <@U02KJG17Q0M|Tanisha Barnett>

CC: <@U0884DN8VGV|Matt Idema>, <@U08202AN90T|Shahzad Shaikh>, <@U08KK7S6LAZ|Diana Williams>, <@W8FHYGK19|Jack Tam>, <@W8FQBMAN9|Andrew Firstenberger>, <@U06KTKYQ2S3|Emma Rodgers>, <@W8F0SN196|Cathleen Ryan (she/her)>
Thread: 31 replies (latest: 2026-02-18 07:33:55 PST)
Reactions: happy_dance (42), rocket-party (32), fire4 (25), catjam-7969 (10), clapping-all (14), lets_go (9)
Files: NO-CC-Happy.gif (ID: F0AEKG8SQNQ, image/gif, 2.9 MB)



---

=== Message from Emma Rodgers (U06KTKYQ2S3) at 2026-02-11 19:32:22 PST === 
Message TS: 1770867142.372729
Amazing work!! :rocket:
Reactions: heart (1)



---

=== Message from Devin Mercier (he/him) (W0132PNAC9X) at 2026-02-12 07:28:14 PST === 
Message TS: 1770910094.843269
:rocket: *Resend to Engaged Non-Openers (RENO) in the Email Checklist Live to 100% of Customers* :slot_machine: 
Low- and mid-tier senders frequently stop short of realizing full campaign impact because they don't follow up with non-openers, or they resend manually to their full list, harming deliverability. Users see "low opens," assume email isn't working, and disengage. We hypothesized that by embedding a frictionless "resend to engaged non-openers" option directly in the email checklist, we could help users extend reach safely and confidently, increase send cadence, and ultimately improve retention.

:chart_with_upwards_trend_intensifies:  *Impact & Metrics:*
The experiment showed a *+4.2% lift in C1s with 2+ sends* (from 40.49% to 42.19%), at *100% probability variant > control*. Users are sending *1.6% more campaigns overall* (1.76 to 1.79 per user) with particularly strong results for *FTUs* (+7.6% in 2+ sends). C1 send rate held flat, confirming the feature complements rather than cannibalizes normal sending behavior. Create-to-send rate dropped slightly (70.04% to 68.28%) but this is expected given scheduled resends are counted as "created" before they're sent - with actual sends up, this isn't a concern. With the movement in our primary metrics we are estimating *$140k in in-year revenue growth* *and $503k for annualized*.

:money_blob: *Side note:* With this recent win, the Core Campaigns team has accumulated an *estimated $1.078M in annualized gains from experiment wins*, _just since November_.

:shoutout1: *Shout Outs & HUGE THANKS:*
<@U02KM9C1V3L|Dalyn Small> <@U04RXGCEPCY|Tracie Kreiss> <@U04739FF7M5|Adam Williams> <@U09FSQCDVK4|Sergio Lopez> <@U04SQQF50DP|Kamrin Kennedy> <@U09B1S1DZ6Y|Sundeep Nadendla> <@U02KZMX4E6M|Celeste Mora (they/them)> <@U07RKQ1P8Q2|Yizhou Qiu> <@U02QFTEHKB9|Kevin Martin>
cc: <@U06QRS4SEBC|Rianna Schanno> <@U08D0C42PJM|Andrew Spitz> <@U08KK7S6LAZ|Diana Williams>
Thread: 6 replies (latest: 2026-02-13 09:49:56 PST)
Reactions: winning-kid (12), fire (11), celebrate (8), clapping-all (6), huge (6), big_dog (2), party_otter-1687 (3)
Files: image.png (ID: F0AE6T30XST, image/png, 312.8 KB), image.png (ID: F0AE6T41YK1, image/png, 290.6 KB)



---

=== Message from Pratik Gupta (U02L0341LMP) at 2026-02-12 07:46:00 PST === 
Message TS: 1770911160.543409
:rocket: `*Launched*: *A Brand New Canva Integration!!!*` :canva-logo: :mailchimp2:

:bulb: _*What We Launched and How It Benefits Customers*_
• _On 1/22, we launched our new *Mailchimp integration in Canva’s App Store*._ This integration allows users to “Publish” point-in-time designs and assets from Canva to our Content Studio. 
• An upcoming iteration will _unlock the #1 feature request from Canva users: the ability to `Push Canva Email designs as HTML emails directly to Mailchimp`!_
:dart: _*Why This Is Important*_
• *Canva Momentum:* 
    ◦ Canva is our leading integration driving ~11.5K NBs and ~$432K in NB MRR FYTD
    ◦ Customers who connect to Canva are _more likely to send emails_ than those who are not (42% vs 28%)
    ◦ The ability to bring dynamic/responsive email designs from Canva to Mailchimp is one of the most requested features.
• *Growth:* With us delivering on this integration in Q2, Canva has agreed to provide us visibility in key GTM motions to help drive customer growth:
    ◦ _Featured listing_ on the header of the Canva app store for the month of February (for Canva users on all plans except Enterprise and Education)
        ▪︎ Image attached since Intuit laptops block Canva by default.
    ◦ Mentions in upcoming marketing activities like the “What’s New” campaign
• *MC Everywhere:* This is a major milestone in our _MC Everywhere_ effort to use partner integrations to reduce customer effort/fricton and improve campaign performance.
:winning-kid: _*How We Measure Success*_
• _New Bookings and Adoption:_
    ◦ Early data shows that we have 17 NBs worth $655 in MRR
        ▪︎ This is for the first few days of release, with no GTM or exposure of any kind.
    ◦ Overall, we’re seeing 2175 C1s already connected to the new integration, of which, 55% (1212) are paid.
• _Email payoff for Canva Connected Users (CCUs):_ too early to report.
:tech-forward: _*Looking Ahead*_
Leading up to and beyond Canva’s primary marketing event of the year in April, <https://www.canva.com/canva-create/|Canva Create> :excite:, we are planning to upgrade the E2E workflow for Canva+MC users to be a *seamless Design-to-Send experience*. This includes:
• Building the HTML Email Import functionality which easily brings Canva designed emails to Mailchimp in a _ready-to-send state_.
• Improvements to _Wayfinding and Discovery_ to ensure C1s can see their work through to sending emails with Canva assets.
:teamwork1: _*Thank You!*_
This effort was a massive undertaking to pivot, develop, and launch in an shortened timeline in order to secure GTM commitments and a competitive advantage with Canva users. A huge shoutout to the following people (apologies if I missed anyone): :shoutout1: 
• *Product:* <@U08DYEMBSSG|Jason Cross>, <@U09979JPH37|Ose Amiegheme> 
• *Engineering:* <@U07AX5J7MFB|Eric Anderson>, <@W8FHXCZSP|Saikat Mukherjee>, <@U02KJFNSB6H|Philip Allen>, <@U02K6LEHGKZ|JB Lovell>, <@U02KJE9JALV|Michael Hawkins>, <@U085B0VAFHV|Nalin Ahuja>, <@U02KEGFKTPG|Cromwel Pestano>, <@U0878AG7GGZ|Max Garceau>, <@U031T5Y29HC|Rohit Mereddy> <@U07A05V0H5J|Stephen Komae>
• *Design:* <@U02KPGZ4HHS|Jane Guthrie>, <@U02KJA0C137|Erin McCue>, <@U03QJC545C2|Ashley Wiesner>, <@U07KKEVS695|Skye Hurley> 
• *TPM:* <@U03R9TTF7FY|Abby Barnett>, <@U07PJK7TTPE|Brooke Addison>, <@U02K6LY0X63|Jessie Brown> 
• *Business Development:* <@U074FPETM5W|James Domenick>, <@U0792U11BDX|Michael Huang> 
• *Marketing:* <@U079XLXJ338|Allie Strack>, <@U08N8T8ME2Z|Bianca Regan> 
• And our friends at *Canva*. :slightly_smiling_face: 
Thread: 3 replies (latest: 2026-02-12 09:35:10 PST)
Reactions: clap-blob (22), rocket (17), fire_hdr (11), canva-logo (4)
Files: Featured Header.png (ID: F0AE6FVQL8P, image/png, 754.6 KB), App Listing.png (ID: F0AE6FXB7U7, image/png, 398.8 KB)



---

=== Message from Stephen Yu (U040C49798T) at 2026-02-13 07:34:36 PST === 
Message TS: 1770996876.843979
:rocket_launching: *Attribution expansion to QBO transaction and Wix booking conversions* :rocket_launching:
We are evolving our attribution service to serve a greater share of user needs by attributing key conversion outcomes to campaign performance. *This creates differentiation for users that demonstrates the value of Mailchimp by truly connecting their campaigns to outcomes that they care about beyond just high level engagement metrics such as opens and clicks.* To achieve this, we created a scalable attribution infrastructure that expands beyond the single-entity Ecommerce order conversion today into multi-entity conversions to also include QBO transactions (invoices, sales receipts, estimates) and Wix bookings, serving the needs of both product and service-based businesses. This enables users to answer critical ROI questions such as 'How many sales receipts did my recent campaigns generate that led to sales? or 'Which of my campaigns generated the highest bookings amount?'.

:customerproblem: *Customer problem:*
*73% of customers indicate that they need support in their marketing strategies and 44% of prospects indicate that ‘How MC could drive results/value for my org’ is an important reason for purchase.* Today, the only available conversion metric is orders but users often have different conversion objectives when it comes to assessing marketing performance. With this change, we are expanding to meet broader user needs by connecting unique data mapped to contacts across QBO, Wix and Mailchimp.

:rocket4:*What was launched?*
*We launched the ability for users with eligible integrations to attribute QBO transaction and Wix Booking events to campaigns that are mapped at the C2 level.* Users will be able to see ROI insights around attributed conversions and attributed conversion amount across Omnichannel campaigns starting in reporting components in homepage and marketing dashboard. Users can also select specific conversion outcomes that they want to measure their campaign performance against and continue to have the ability to customize attribution settings such as attribution windows across email and SMS channels. In addition, this work enables us to flex into future conversion attribution work. We are testing this experience to track downstream metrics

Who is this available for: Users with Wix integrations and users connecting new QBO integrations.

Resource: <https://www.figma.com/design/EXtOXQxBS4v72WwWVKFX3t/Omnichannel-analytics?node-id=1485-11560&p=f&t=y1ZDJQ9B6NT6ZAcN-0|Design>, <https://docs.google.com/document/d/1LZzV4OxMQDjrDH5xa_HxOAGmfWzyBaSA1wvZtJ7UKIo/edit?tab=t.0#heading=h.4c40og9ra3k3|Test plan>, <https://docs.google.com/document/d/18T75zrj1q4TPzAYP7NM3SpASVIsh1DAhNPpf9ZUbGIM/edit?tab=t.0|PRD>

:chart_with_upwards_trend: *Impact and Metrics*
• *Evolve from 1 conversion metric that is difficult to scale to 5+ conversion metrics and reporting that can scale* 
    ◦ *This also brings us to parity with competitors like Klaviyo that can handle multiple conversion outcomes*
• *Enable more cohesive and integrated experience across QBO and Mailchimp,* leading to competitive differentiation and ladders up to the broader strategy of one Intuit platform
• *Drive actions such as campaign sent:* Increase in campaigns sent from building user confidence through attributed conversions
• *Attributed revenue*: Increase in % of attributed revenue from campaign conversions
:next: *What’s next?*
We will continue to scale into a broader range of conversion outcomes to include 1P Pixel events and the ability to define custom attribution conversions. This is also the first of many steps to create differentiated experiences across Mailchimp and QuickBooks, leading to unique competitive moat that provides customer and business value.

:megaphoner-1707: *Shout outs & HUGE THANKS*
This was a huge undertaking to create a durable platform to accelerate marketing performance - a huge thank you to the cross-functional teams who worked diligently to champion user needs!!

Engineering: <@U02K6FKBG31|Benjy Phillips> <@U046WDQCP0R|Cavin Myers> <@U07H6LXGTRC|Sangara Naarayanan> <@U06NZ7W5L2V|Santhosh Ragavu> <@W01108SHDV4|Sarvesh Kumar> <@U03EEL3PU9H|Sid Kumar>
Design: <@U02KMFKKDU2|Sahana Srivatsan>
Product: <@U040C49798T|Stephen Yu>
TPM: <@W8GG78R1C|David McDonald>
Data Science: <@U07ED705DHS|Aastha Sehgal> <@U0970UUFN80|Ashish Prakash>
Product Marketing: <@U03HRFYTYUB|Simone Kovacs>
Wix Integration: <@U04925BQ27M|Ade Ajanaku> <@U0878AG7GGZ|Max Garceau> <@U02KEGFKTPG|Cromwel Pestano>
QBO Integration: <@U09A9P01S4F|Nick Triscritti> <@U03TDGU2JUB|Josh Day>
cc <@W8FHXCZSP|Saikat Mukherjee> <@W8FL6URHQ|Deepak Prabhakaran> <@W8Z8R7STE|Nir Harel> <@U03EEL3PU9H|Sid Kumar> <@U02KPGZ4HHS|Jane Guthrie> <@U0970UUFN80|Ashish Prakash> <@U09QF7F45AQ|Nathan Snell>
Thread: 6 replies (latest: 2026-02-24 11:54:12 PST)
Reactions: rocket (17), launch-131 (6), nice-pink (2)
Files: image.png (ID: F0AF0CMQPK6, image/png, 156.7 KB)



---

=== Message from Amanda Hunt (U02LARVGVGQ) at 2026-02-16 12:31:57 PST === 
Message TS: 1771273917.718519
Hello, everyone! Sending an update on the No CC V2 experiment:

*The Issue:* 
• On Friday, 2/13, the team identified that experiment context and purchase intent from dotcom was not being appropriately passed into account setup if the customer created an account from GSSO. 
• This meant that *any customer* who picked a paid plan from dotcom would not have that selection stored once their account was created - they would be shown paywalls again during account setup and have to reselect. 
• Unfortunately, this looks to be a long standing issue with GSSO created accounts. 
*The Impact:* 
• While this issue impacted all customers from dotcom, it was discovered in the context of *No CC V2.* 
• Customers who were activated into the No CC V2 experiment from dotcom and then used GSSO to create their account would *not* see No CC experiences during account setup - they were always shown the baseline paywall that requires a CC 
• This issue happened from both the GSSO modals on dotcom (experiment context dropped) or from the account creation page (experiment context + purchase intent dropped). 
*The Fix:*
• The team worked over the weekend to identify the issue and fix the issue. The issue is resolved as of Monday, 2/16
*What this means for No CC V2:* 
• Since a significant portion of prospects use GSSO to create accounts, we will be updating experiment dashboards to reset our No CC V2 data to start tomorrow, 2/17 (the first full day after the fix) 
:ty_: A HUGE thank you to the team who mobilized quickly and went above and beyond to get this resolved for our customers. <@U04C207T80Z|Italo Carillo>, <@U032WKWKF2P|Harshada Desai>, <@U045QK7AM1A|Anesia Smith>, <@U02KEAE3DL6|Bryce Hammond>,<@U02URC9KK46|Lawrence Ma>, <@U07TMNHQ20N|Phuong Trang>, <@U07QYRC1V54|Prabhakar Venkatesan>, <@U02KPENAJ0L|Chris Whyte>, <@U05NALW1S3U|Collins Amadi>, <@U02KM08JQR0|Aaron Armstrong>, <@W8GN4BUBH|Danh Dang>, <@U047HMUGE82|Erin Szarpa>,  <@W8FM8V11S|Jed Apostol>, <@U08N2BTNV46|Jennie Zhou>, <@U06K8UTTSJE|Jing Wang>, <@U02V0Q6K27P|Yilmaz Kara>, <@U02KZMMUN2V|Allison Lizza>, <@U02ATLVNQCV|Hrishikesh Babar>

CC: <@U0A99U871KR|Sid Bakhru>, <@WB6QH3S20|Christine Kuo>, <@U0A8293TH9U|Anish Nahar>, <@W9GLZQ45A|Ryan Tuosto>
Reactions: blob-heart (8), thankyou1 (4), thankyouu (1)



---

=== Message from Jing Wang (U06K8UTTSJE) at 2026-02-16 12:34:20 PST === 
Message TS: 1771274060.019569
Thanks team for fixing this over the weekend
Reactions: heavy_plus_sign (1)



---

=== Message from Emma Rodgers (U06KTKYQ2S3) at 2026-02-17 13:31:38 PST === 
Message TS: 1771363898.180299
Thank you for the continued diligence and moving quickly on the fix. 



---

=== Message from Elizabeth Bertasi (U06QWR7FV9T) at 2026-02-23 12:08:52 PST === 
Message TS: 1771877332.494119
:rocket: :cjb: :new: *New abandonment triggers launched!*

:search-pin: *What’s new?* 
2 weeks ago, we released new abandonment-related automations triggers to help our C1s recover sales from their high-intent contacts. These include browse abandonment, which fires when a contact looks at a product but does not add it to their cart, and true cart abandonment for Shopify, which fires when a user adds a product to their cart but does not initiate check out. These supplement our existing abandonment triggers, Shopify checkout abandonment (now renamed to more clearly differentiate it from cart abandonment) and non-Shopify cart abandonment.

These triggers are incredibly high-value for ecomm customers - we’ve unlocked automated email and messaging higher up the funnel for maximum reach.

:analytics-graph: *Impact & metrics:*
• In our experiment variant, we saw 62 C1s create a true Shopify abandoned cart automation and 13 turn it on, and 32 C1s create an abandoned browse automation and 6 turn it on.
• <https://tableau.a.intuit.com/#/site/MChimp/workbooks/74898/views|Bayesian experiment dashboard>
• <https://app.amplitude.com/analytics/intuit-portfolio/dashboard/lbc52vk4|Automations trigger expansion Amplitude dashboard>
:coming-soon-icon: *What's next?* 
We’ll get laser-focused on increasing adoption of these features so our users can see real value, and we’ll measure C1 business impact for those adopting these features. We’ve converted this experiment to a back test so we can continue to measure impact over time as adoption compounds.

:clap: :clap: *Shout outs -* as with all the releases in the DSB effort these past couple weeks, this super cross-collaborative and required hard work from many folks - thank you to everyone involved! (and if I have missed any names please let me know so I can add!):

Automations: <@U09BAMA1N9X|Nakul Lahoti> <@U03GVFDGUKA|Cliff Martin> <@U02KMGM5D98|Yena Ku (they-them)> <@U02KJ1UDHC5|Bobby Craig> <@U03GE2Y59M0|Dana Winn (Automations Oncall)> <@U02KZU660AV|Jameson Brown> <@U02KMC0QGSW|Justin E. Samuels> <@U07UCSZSA30|Keith Ferney> <@U02KMDU1TU2|Maxwell Reich> <@U07NA0QPYJ0|Saisharath Peddibotla><@U07UY6KBVNV|Rob Berryhill> <@U09LKQLTUF4|Swati Pawar> <@U09RVPBJE1G|Alex Gutierrez> <@U02P9STSQGZ|Becca Walsh> <@U02KZMX4E6M|Celeste Mora (they/them)> <@U02KMBDS7AP|Heather Dartz>  <@U06QRS4SEBC|Rianna Schanno> <@U02KJBP43V3|Jess Riddle (She/Her)> <@U02KJ5X1V3P|Cary Duncan>  <@U07RKQ1P8Q2|Yizhou Qiu>
Integrations: <@U095D83P9UN|Louis Pan> <@U02KM2QGKEW|Ali Heidary> <@U09E6FWDJSK|Vahid> <@U09U6117EG0|Martin Madiri> <@U02KJFNSB6H|Philip Allen> <@U079Y3PKJLQ|Vassilis Dourdounis> <@U07PJK7TTPE|Brooke Addison> <@U03R9TTF7FY|Abby Barnett> <@U02KMBTRKL2|Jenna Fitzpatrick> <@U03TANAE9AR|Spencer Reynoso>
Email: <@U09979JPH37|Ose Amiegheme> <@U03TC2MB06M|James Arama> <@U04SYBP56JZ|Michelle Ducote> <@U02KJE9JALV|Michael Hawkins> <@U02KJA0C137|Erin McCue> <@U02K6LEHGKZ|JB Lovell>
SMS: <@U02KPE15PCL|Connor Callahan> <@U02KJEHK677|Neil Desai> <@U03NU55364D|Satish Sambandham> <@U04QZ1RRPLN|Ty Kuhn> <@U0946BZ3QTW|Mike O'Dell> <@U03V70QRTRQ|Mythili Gopikanth> <@U07T1UYE259|Rick Barker> <@U0703THQZRQ|Gary Aloisio>
CDP:  <@U04NGRG0RH9|Lauren Colwell> <@U07GRQTTY30|Arkesh Rath> <@U07146FU35X|Jeffrey Li> <@U04SC218QQ3|Sijia Liu> <@U078B7PT3A8|Dan Damkoehler>
DSB: <@U079SMT5UTA|Matt Cimino> <@U086MMX7W0M|Juliana Simoes> <@U02K6PULZQX|Pooja Berrong>
<@U08KK7S6LAZ|Diana Williams> <@U07AX5J7MFB|Eric Anderson> <@W8FHXCZSP|Saikat Mukherjee> <@W8FHYGK19|Jack Tam> <@W8FQBMAN9|Andrew Firstenberger>
Thread: 5 replies (latest: 2026-02-24 05:33:25 PST)
Reactions: big_dog (16), woo (12), clap (16), clap::skin-tone-2 (2), rocket_launching (21), yay-pink (4), clap::skin-tone-3 (2), clap::skin-tone-4 (1)



---

=== Message from Payton Camilli (W012EU6L7FG) at 2026-02-24 09:15:43 PST === 
Message TS: 1771953343.418679
:rocket_launching: *LAUNCHED - SMS Webhooks* :rocket_launching:

:question:*What changed?* SMS users can now set-up webhooks for the following contact update types `SMS subscribed`, `SMS unsubscribes`, `SMS phone changed`, `SMS campaign sending`

:clap-clap: *Why is this a big deal?*
        ▪︎ In the first month, 2173 C1's have begun using the new hooks, mainly via the API. We've fired over 400K SMS webhooks total.
        ▪︎ Webhooks close the automation gap between email and SMS so customers can run the same level of automated workflows on both channels.
        ▪︎ The capability was built to power 2-way sync for Shopify as part of the recent DSB launch, but we shipped to 100% of users so the whole base can benefit.
:books: *Resources (*<https://mailchimp.splunk.intuit.com/en-US/app/search/aorg_-_webhooks?form.global_time.earliest=-24h%40h&form.global_time.latest=now|Splunk> & <https://docs.google.com/document/d/1VnFzc5vhqF7sE5keRIZ_3SGiHabgy5sI6Azuw3yR2ds/edit?tab=t.qqspvv4tg5y9#heading=h.tzhoo5fxa6yo|PRD>)

:next: *Whats next?*
    ◦ Iterate based on user feedback
    ◦ Work with CSMs to onboard more users! Message us in <#C09UN5PCAN4|mc-aorg-prj-sms-webhooks> if questions pop-up.
:mega: *Who made this possible?* :mega:  :star2:<@U02KMFE1ELT|Rolf Martin-Hoster> :star2: <@W019Y5V05UG|Mohammad Habbab> <@W012EU6L7FG|Payton Camilli> <@U07USKD0MA5|Shefali Dalal> <@U04FF36UREJ|Lina Lozano Oviedo> <@U02LB4VC4UQ|Nate Ranson (he/him)> <@U04D7TX5LDB|Ryan Hungate> <@U035AGFSBRC|Sabrina Harris> <@U02KJFNSB6H|Philip Allen> <@W8FHXCZSP|Saikat Mukherjee>
Thread: 1 replies (latest: 2026-02-24 10:25:50 PST)
Reactions: blob_cheer (17), clapclap (9), heart (2), face_with_cowboy_hat (2), perfecto2 (1), raised_hands (1)



---

=== Message from Elizabeth Bertasi (U06QWR7FV9T) at 2026-02-25 11:59:45 PST === 
Message TS: 1772049585.802789
:rocket: :cjb: :new: *New messaging behavioral triggers launched!*

:search-pin: *What’s new?* 
We released 2 new SMS-specific automations triggers, “Sent a message” and “Clicks a message link.” Marketers currently lack granular behavioral triggers for messaging channels. This gap prevents them from creating real-time, personalized follow-up campaigns based on how contacts interact (or fail to interact) with their messages, and represents a gap in utility between SMS and email on our platform today. These two new triggers begin to close that gap to provide a best-in-class automated SMS platform.

:analytics-graph: *Impact & metrics:*
• This has been launched as a back test, so we’ll measure impact over time and see what we can improve.
• <https://app.amplitude.com/analytics/intuit-portfolio/dashboard/lbc52vk4|Automations trigger expansion Amplitude dashboard>
:coming-soon-icon: *What's next?* 
In the coming weeks, we’ll launch 2 additional messaging triggers (“Doesn’t click message link” and “Contact sends a message”) to complete our messaging triggers workstream. We’ll get also work on increasing adoption of these features so our users can see real value, and we’ll measure C1 business impact for those adopting these features. This has been launched as a back test, so we’ll continue to measure impact over time and see what else we can improve.

:clap: :clap: *Shout outs -* thank you to everyone who worked together to make this happen! (and if I have missed any names please let me know so I can add!):

Automations: <@U09BAMA1N9X|Nakul Lahoti> <@U03GVFDGUKA|Cliff Martin> <@U02KMGM5D98|Yena Ku (they-them)> <@U02KJ1UDHC5|Bobby Craig> <@U03GE2Y59M0|Dana Winn (Automations Oncall)> <@U02KZU660AV|Jameson Brown> <@U02KMC0QGSW|Justin E. Samuels> <@U07UCSZSA30|Keith Ferney> <@U02KMDU1TU2|Maxwell Reich> <@U07NA0QPYJ0|Saisharath Peddibotla><@U07UY6KBVNV|Rob Berryhill> <@U09LKQLTUF4|Swati Pawar> <@U09RVPBJE1G|Alex Gutierrez> <@U02P9STSQGZ|Becca Walsh> <@U02KZMX4E6M|Celeste Mora (they/them)> <@U02KMBDS7AP|Heather Dartz> <@U06QRS4SEBC|Rianna Schanno> <@U02KJBP43V3|Jess Riddle (She/Her)> <@U02KJ5X1V3P|Cary Duncan> <@U07RKQ1P8Q2|Yizhou Qiu>
SMS: <@U02KPE15PCL|Connor Callahan> <@U02KJEHK677|Neil Desai> <@U03NU55364D|Satish Sambandham> <@U04QZ1RRPLN|Ty Kuhn> <@U0946BZ3QTW|Mike O'Dell> <@U03V70QRTRQ|Mythili Gopikanth> <@U07T1UYE259|Rick Barker> <@U0703THQZRQ|Gary Aloisio> <@U03J3GGU5T3|Jeremey Nofzinger> <@U09PS80BY85|Mesam Haider> <@U03TDLSFYH0|Ben Marks> <@U044UN28H6C|Sreeram Jayan><@U076PQ83WPJ|Ana Bell>
DSB: <@U079SMT5UTA|Matt Cimino> <@U086MMX7W0M|Juliana Simoes> <@U02K6PULZQX|Pooja Berrong>
<@U08KK7S6LAZ|Diana Williams> <@U0ACRAXEK7T|Mani Dhillon> <@U07AX5J7MFB|Eric Anderson> <@W8FHXCZSP|Saikat Mukherjee> <@W8FHYGK19|Jack Tam> <@W8FQBMAN9|Andrew Firstenberger>
Thread: 3 replies (latest: 2026-02-27 09:44:22 PST)
Reactions: wedidit7 (14), mc-sms (7), blob_cheer (15), ship (4), tada (7), great-job-team (2), party-cat (2), raised_hands (1), yay-frog (1), dance_vibe (1), dancedoggo (1), white_check_mark (1), rocket_launching (1)



---

=== Message from Deeti Chavda (U03LYEV0VH9) at 2026-02-27 07:00:09 PST === 
Message TS: 1772204409.021839
:rocket: *Launched| Spanish Phone Support & Intent-Based Saves Pilot* :rocket:
*Opportunity:* As Mailchimp expands internationally, our Spanish-speaking customers particularly those on non-Premium paid plans have lacked an immediate high-touch phone channel. Without specialized retention routing, we were missing critical opportunities to intervene when these customers signaled an intent to churn, potentially leading to avoidable losses in the Spanish market. To solve this we are introducing a 3 month pilot designed to intercept those signals and prove the ROI of localized retention efforts in the Spanish market.

*What we launched* :dart:
• Expanded Phone Support: Enabled "Call Me Now" and "Scheduled Callback" options for eligible Spanish-speaking customers on all paid plans (Legacy, Essentials, Standard, and PAYG).
• Intent-Based Saves Routing: Implemented Saves effort via CUP keyword detection. When a user searches for churn-related terms like _"cancelar plan,"_ they are now prioritized and routed directly to a specialized Saves queue.
• Bilingual Support Operations: Leveraged existing bilingual experts to provide real-time assistance during business hours (7:00 am – 11:00 pm GMT).
*Why it matters* :sparkles:
• Expanded Reach to At-Risk Customers: The initiative significantly broadens access, moving from a small subset of high-spend users to the vast majority of our 40,000 Spanish customers on paid plans.
• Targeted Churn Interception: By implementing intent-based routing (CUP keyword detection), the system can proactively identify and intercept critical churn signals.
• Operational Validation: This pilot allows the team to validate the capacity, staffing, and routing logic required for a potential full-scale international rollout.
• Inclusion and User Experience: It eliminates the previous restriction where sub-$299 spenders were limited to Chat and Email, providing a more inclusive and high-touch experience for the broader Spanish market.
*Business impact* :white_check_mark:
We expect this pilot to validate that high-touch support for the Spanish market directly correlates with improved retention. Early signals from our first two weeks (Feb 12 – Feb 25) show strong momentum and rapid operational scaling:
• Volume Growth: Total "Call Me Now" volume increased 91% week-over-week and specialized Saves interactions nearly doubled reaching 15 in just the second week.
• Efficiency Gains: Our Issue Resolution rate surged from 33% to 83% in the second week as experts hit their stride.
• Operational Health: We achieved a 94.9% Handle Volume in Week 2, ensuring nearly every Spanish customer who reached out was connected to an expert.
*Who’s impacted* :busts_in_silhouette:
This expansion scales phone support to nearly 40,000 Spanish-speaking accounts, targeting all active paid users in the `/es/` environment with spend recorded in the last 30 days. By lowering the threshold to any paid plan with >$0 spend, we are significantly broadening our high-touch support footprint in the Spanish market.

*What changed (before / after)* :arrow_left::arrow_right:
• Before: Phone support was restricted to high-spend Premium customers only; no specialized retention routing existed for Spanish customers on any paid plans.
• After: Phone support is now visible to all eligible Spanish customers on paid plans during business hours, with automated routing that prioritizes "Saves" interactions over general inquiries.
*Thank you* :tada::raised_hands:
Bringing this pilot was no small undertaking, and it wouldn't have been possible without everyone’s expertise and tireless effort to get it across the finish line. A huge thank you to everyone who designed, tested, and shipped this experience to ensure our international customers have a reliable, bilingual path to support when they need it most and apologies if I missed anyone!
*PD:* <@U02KEED6LTG|Ankur Bag> <@W8F0T38P2|Nicholas Buddenbrock> <@U02KJ3JU2LV|Alvaro Bueno> <@W8FL2R1J6|Roopesh Sheth> <@W8FMBUYCU|Tim Ulibarri>
*Modern Ops:* <@U09JUEWFB2S|Carter Bishara> <@U02KZUTQZQR|Heather Bryant> <@U03V5R04SQ7|Brett Richards> <@W7SV76CN5|George Ware-Expert Ops-GBSG Strategy and Execution>
*Customer Success:* <@U02KP90J3K6|Ben Davis> <@U02KJB1E59T|James Eustice> <@U03FWD0U69J|Sandra Gibbs> <@U02KJ9Q6PL5|Daniel McClendon> <@W8GG89822|Fiona Mack McNab> <@U04HV6718PK|Kavita Shial> <@U02LB711L0G|Tyler Ward>
*Staffing and Training:* <@U02KZQWG5GR|Anna Dang> <@U084ZTZF15E|Faye Harris> <@U057J63LDNW|Stefanie Hernan>
*Analytics:* <@W8FHWDUUB|Wendy Anderson> <@U05E269C7FH|Dev Parikh>
Reactions: 100 (13), party-phone (13), celebrate (14), fire (14), spanish (9), woo (9), huzzah (8), aw-yeah (7), clapping-all (10), yay (1), lesss-go (1), ohyeah-625 (1)



---

=== Message from Jacquelyn Horgan (U02KMAN6V1R) at 2026-02-27 09:48:22 PST === 
Message TS: 1772214502.795949
:rocket: *Oman Tax Registration* :money-bag: 

:search-pin: *What’s new?* 
Effective March 13, 2026, we'll begin collecting Value Added Tax (VAT) at a rate of 5% on transactions for accounts operated in Oman. This applies to B2C transactions. B2B's can opt into reverse charge by providing a valid VATIN at on checkout or at <http://mailchimp.com/account/billing/info/|mailchimp.com/account/billing/info/>

:analytics-graph: *Impact & metrics:*
Timely registration and development is revenue protective:
• Taxes, Penalties and Interest (TP&I) estimated at *$113K* :not-today-satan: 
• 2025 Sales to Oman was *$122k ARR* w/growth of *6% YoY* :chart-increasing: 
:dream_team: *Launched by:* Mailchimp Monetization FINOPS Squad
:clapping-all: *Shout outs:* <@U06RXPP6HNU|Nikhil Kassetty> <@W01BKFS7N8P|Navreet Kaur> <@U08DG6TKGGP|Patrick Khoo> <@U02KMGYSHK4|Victoria Velarde>
Thread: 1 replies (latest: 2026-02-27 12:33:24 PST)
Reactions: checkgreen (5), ohman (2), celebrate-inclusive (3), rocket (2)



---

=== Message from Stephen Yu (U040C49798T) at 2026-03-02 08:13:39 PST === 
Message TS: 1772468019.988369
:robot2::rocket_launching: *Analytics Agent V1 (Project Alfred) test update*

Today, businesses are heavily time-constrained and often lack marketing expertise to effectively maximize their marketing performance. *They spend hours manually analyzing performance*, with 53% of SMBs immediately investigating unusual performance and 38% dedicating weekly time to analyzing campaigns. To address this need*, we recently <https://intuit-teams.slack.com/archives/C03TLJNADSP/p1766089915729689|launched the first version of the analytics agent> that acts as an AI-powered analytics expert by your side natively within Mailchimp that transforms fragmented marketing data into insights and data-backed recommendations through an AI-native conversational experience.* Through this change, we are evolving from static passive reporting into proactive intelligence to inform next steps.

We launched this as an A/B test to an initial cohort of 50K users and are seeing *lift on our primary metric and other key downstream metrics.*

:impact:*Impact & metrics:*
• *+6% to email campaigns sent per user* from 2.69 to 2.86 (>99% prob. to beat control)
• *+0.7% to % of users sending 1+ email campaigns* from 70.1% to 70.6% 
• *We are also seeing positive trending in downstream metrics* around r*eduction in active churn* and i*ncrease in % of MC attributed revenue* 
In addition to these results, we continue to see *strong adoption and customer sentiment* of:
• *85% engagement* when users viewed analytics agent 
• *3000+ insights generated to date* for users 
• *Hear from our customers directly:*
    ◦ _"The AI gives me a depth of intelligence and analytics that is eye opening. Plus it summarizes without me having to go in and do it myself."_ 
    ◦ _"The responses were in depth and synthesized the data for me clearly."_
    ◦ _"The information that it is providing is really valuable and it would take a ton of time to come up with this information and the suggestions on my own."_
We also identified an <https://docs.google.com/presentation/d/1kaiLDCgMTEOIhU9V-LHPr5Ms5IihLMWDugTU1Ctkldc/edit?slide=id.g3cbb636fcad_3_13#slide=id.g3cbb636fcad_3_13|opportunity> to leverage this capability to *solve custom analytics requests from HVC / High churn risk customers.* Along with CSM, *w*e applied this approach recently to a *churn risk user (1300 MRR) with a custom reporting request* that would typically take weeks to build and solved it instantly with great customer feedback.
• *From: Custom reporting requests that* *take weeks/months to build that is not scalable* to other users through static reports 
• *To: Tailored insights in seconds* based on exactly what customers are looking for 
:checkgreen: *What’s next:*
We will be building on this momentum to test and scale to a larger group of users in 2 weeks for our v2 (beta) test all built through AI-native experiences. This will include end to end improvements:
• Built on durable and performant data platform with expanded data coverage (SMS, Ecomm funnel)
• Enhanced data understanding layer with improved agent eval and accuracy scores 
• Improved user context with C1 profile info 
• Enhanced user experience with streaming, conversation history and data visualizations 
:clap: Thank you to everyone who made this possible and continue to deliver innovative experiences to our customers (Apologies if I missed anyone!). *Engineering:* <@U01J5GVP5GV|Kuntal Naphade> <@U09Q9KFSP8W|Jason Dudley> <@W8FMAA7S8|Yi Zhang> <@U08ALKME0VA|Inder> <@U0428EDN518|Nick Boyle> <@U03EEL3PU9H|Sid Kumar> <@U04QNS5KEE6|Ajeet Seenivasan> <@U07B02LLNAC|Dmitri Medvedev> <@U09SU5ERJET|Sreekanth PS> <@U09UW0PFAG4|Rose Therese> *AI science:* <@U0793KXBF51|Bryan Smith> <@U02KM30QU10|Ben Leathers> <@U07SEHWU9AN|Nithali Sridhar>  *Product:* <@U040C49798T|Stephen Yu> *Design:* <@U02L04W0FPT|Tamlin Tromp>  <@U02KJ9QRSDT|Eddie Shrake> <@U0372SDKQDS|Tiffany Huang> *TPM:* <@WP0ENL12Q|Deepak Mirani> <@W8GG78R1C|David McDonald> *Data science:* <@U0970UUFN80|Ashish Prakash> <@U07ED705DHS|Aastha Sehgal> <@U03BZL23C1F|Heuisu Kim> *Product marketing:* <@U03HRFYTYUB|Simone Kovacs> <@U096DLJK8NA|Jonathan Rodgers>
cc <@W8FHXCZSP|Saikat Mukherjee> <@U08ALKME0VA|Inder> <@U064FLW0QAK|Taylor Horton> <@W8FL6URHQ|Deepak Prabhakaran> <@U02KPGZ4HHS|Jane Guthrie> <@W8Z8R7STE|Nir Harel> <@U08KK7S6LAZ|Diana Williams> <@W8FHYGK19|Jack Tam> <@W8FQBMAN9|Andrew Firstenberger> <@U09QF7F45AQ|Nathan Snell>
Thread: 2 replies (latest: 2026-03-02 09:02:52 PST)
Reactions: tada (22), raised_hands (8), cool-doge (7), raised_hands::skin-tone-3 (2), cat_clap (2), raised_hands::skin-tone-4 (1)

---

=== Message from Laurie McGowan (U02KMCPC99R) at 2026-03-04 09:22:15 PST === 
Message TS: 1772644935.911619
:freddie_tv: *Learnings from Mailchimp's Innovation Council meetup | Audience, Segmentation, and AI*
We recently met with our Innovation Council, composed of 25 of our highest value customers, prospects and agency partners.  Members were split into :digit-five_35: breakout groups (Ecommerce, Professional Services, Other ICP (Tech, Ent), Strategic Partners, and Growth Partners, and we facilitated an extended, 2-hour workshop to learn more about their approach to Audience, Integrations and Segmentation.  Check out the <https://docs.google.com/presentation/d/106csJdh9MQP_iRz8M4uGLkQ-XljZY4GUva91lZshQXc/edit?usp=sharing|cheat sheet> for additional context.

In it, we learned:
• *Across all five groups, participants are not blocked by lack of strategy, ambition, or imagination. They lack infrastructure confidence. What they are blocked by is:*
    ◦ *Fragmented data ecosystems*: Retail, online store, rewards, and analytics data are all structured differently and require manual cleaning.
    ◦ *Weak or inconsistent integrations*: CRM integrations with Mailchimp are seen as “spec-sheet deep” and middleware (Zapier) is widely used due as a patch. CMS integrations are seen as an unlock.
    ◦ *Manual normalization and reporting toil*: Custom properties and integration gaps force manual workarounds. Retail data requires renaming/reformatting before being usable. Journey reporting at present is piecemeal and manually consolidated.
    ◦ *Lack of a trusted, unified source of truth*: Across all groups, the aspiration is for unified customer data with an AI-queryable "second brain" — with some envisioning Mailchimp itself becoming this central source of truth. Ecomm in particular see CDP foundation for omnichannel identity resolution.
    ◦ *AI trust boundaries*: All groups universally agreed that AI is welcome when it assists in cleaning data, normalizing formats, surfacing insights, suggesting actions, and flagging high-value segments. However, AI is strongly resisted when it acts autonomously, generates creative without human control, or touches sensitive data, making transparency and human approval essential for adoption.
• *Key friction points differ by vertical*: Ecommerce groups prioritize omnichannel identity resolution (online/offline stitching); Professional Services focuses on funnel efficiency and external intent signals; Strategic Partners emphasize attribution sequencing and schema normalization; Growth Partners deeply challenge the contact-centric model, requiring group- and account-level intelligence for B2B scenarios.
• *They know how they want to segment and personalize. The common aspiration is the need for a centralized, trustworthy intelligence layer and supports human-guided AI.* Specifically one that: normalizes data automatically, maintains context across tools, understands real customer journeys, supports group and account logic, surfaces insights proactively, and keeps humans in control.
:pin-warroom: *Resources*
Check out our full takeaways, recordings, transcripts, Figmas and more below:
• :slidedeck: <https://docs.google.com/presentation/d/1B6E9FdMiCemc6y18NZM61gV-kCi_egHtMO9xXTZixK4/edit?slide=id.g3c8a102d6a9_0_507#slide=id.g3c8a102d6a9_0_507|Second MIC Meetup Takeaways> - See the full deck of learnings, group nuances, interview clips, and more
• :figma: <https://www.figma.com/board/fvtU7DdRc8TYoYT3CcUytN/FY26-MIC-Session-2?node-id=0-1|Figma> - See how they mapped their data flows today and what they expect in the near- and long-term for data improvements and where AI is most and least welcome
• :heymarvin: <https://app.heymarvin.com/projects/50061/files/|Hey Marvin> - For Recordings and Transcripts
• :slidedeck: <https://docs.google.com/presentation/d/13JYXM72T4tdUx_XV3G25Xu1v02dfvJmAZIfRJsXvNo0/edit?slide=id.g34532690c16_1_2275#slide=id.g34532690c16_1_2275|First Meetup Takeaways> - Dig into the full learnings from our first meetup in September
• :slidedeck:<https://docs.google.com/presentation/d/1Euzk0oG6-qs_1wx9fkg4ryDQwxkGot6gksuX8ABkwOc/edit|MIC Guide> - Learn more about the program and see full member profiles
Lastly, be sure to check out the 2/20 UXR Customer Watch Party, where we shared what we learned, watched clips from each session and facilitated a live discussion with members across research, product, and design: <https://docs.google.com/presentation/d/1gFiLR2I8r8a3WO9VTAgEOLg8TXrtox2reBDqExeeG5Q/edit?slide=id.g3c99e0ade55_5_1#slide=id.g3c99e0ade55_5_1|Recording> | <https://docs.google.com/presentation/d/1gFiLR2I8r8a3WO9VTAgEOLg8TXrtox2reBDqExeeG5Q/edit?slide=id.g3c99e0ade55_5_1#slide=id.g3c99e0ade55_5_1|Slides> | <https://www.figma.com/board/xYaAyugX4gH7nCOHuTxbGY/UXR-Customer-Watch-Parties?node-id=7-1991&p=f&t=hK64YxlGDIIlhhlo-0|Figma>

:shoutout1: *Shout outs & HUGE THANKS*  :shoutout1:  *to our planning and facilitation leads <@U02KANEDWM9|Hannah Graffeo>* *<@U06TEFC1ZSR|Kelsie Martin>* *<@U02KEAWH2KY|Alex Dao>* *<@U02K6AYF0JK|Aylor Brown>* *<@U02L03X7BFB|Rachel Dagley>* *<@U02KPJVRQ9J|Luisa Botelho>*  :extreme-teamwork: 
This group helped organize the sessions, develop discussion guides and activities, moderate conversations live, and put together all of our amazing findings — championing customer obsession!
Reactions: awesome_sun (12), interesting-8285 (2), clapping-all (5), eyes (1), thankyou1 (2)



---

=== Message from Jenny Fukumoto-Pasko (she/her) - Central Time (U036TSTJDRU) at 2026-03-09 11:52:39 PDT === 
Message TS: 1773082359.558589
:rocket::mailchimp: :cashback: *Launched: FY26 Mailchimp x Amex Cash Back Test* :rocket::mailchimp: :cashback:
We are officially LIVE with our Mailchimp Amex cash back acquisition test! Running through May 31, this experiment tests whether higher-value, cash incentives can scale Mailchimp bookings, as it has done for the TurboTax and QuickBooks businesses.

:goal:*The Strategy:*
• *Target:* US Amex small business cardmembers with no Mailchimp spend in past 12 months
• *The Offer - A/B test:*
    ◦ Offer A: Spend $20 or more on Mailchimp, get $5 back (up to 2x) ←_this is what we tested in FY25_
    ◦ Offer B: Spend $20 or more on Mailchimp, get $20 back (1x) ← _for QBO, “Spend $15, get $15” is our winning offer_ 
• *Goal:* Drive 600–1,300+ NBs (new bookings) with a target CAC of <$20.
:chart_with_upwards_trend: *Early Results:*
• *In just 10 days, 95,000 cardmembers* :celebrate-incl: *have enrolled in the offer (by clicking “Add to Card”)* _(this is a very positive indicator, considering in FY25 we ran a 3-month test that generated 60k enrollments total_:merr-sprout:_)_ 
:pray: *Special Thanks:* Huge shoutout to the team who helped make this test possible, being patient with me as I got up to speed on Mailchimp (I’m originally a QBO gal:cool-pineapple:) : <@U03KTG1CABV|Tyler Baugh> <@U033CC0AUD8|Caroline Josey> <@U02LARVGVGQ|Amanda Hunt> <@W8FMB5WKW|Barb Magner> <@U05QNVD0KHP|Cuc Le> <@U032GEW7U0Y|Brent Hallinger> (exec support from <@U079XLXJ338|Allie Strack> <@U06KTKYQ2S3|Emma Rodgers> <@U0888L0S207|Matt Holcombe>)
Thread: 1 replies (latest: 2026-03-09 12:05:29 PDT)
Reactions: raised_hands (9), amex-3859 (8), raised_hands::skin-tone-2 (2), rocket (6), cashback (5), checkgreen (1), watwow (2), raised_hands::skin-tone-3 (1)



---

=== Message from Jacquelyn Horgan (U02KMAN6V1R) at 2026-03-09 12:58:52 PDT === 
Message TS: 1773086332.476069
:rocket: *Ghana e-Invoicing* :money-bag: 

:question-ids: *Wait, what's e-Invoicing?* 
e-Invoicing requires (near) real-time reporting of sales and tax data with the tax authorities. The purpose is to combat tax evasion, streamline auditing processes, and ensure accurate revenue collection. Without eInvoicing, sellers share sales and tax information at the end of the reporting period e.g. monthly, quarterly etc.

Over 100 countries require some form of eInvoicing e.g. B2B, B2G, cross-border sales and real-time reporting. This trend is expected to continue (it's the future!), and is expanding to non-domestic sellers like Mailchimp.

:search-pin: *What's new?*
With this launch, we will are now real-time reporting transactions to the Ghanian Revenue Authority (GRA) via the Fonoa API. Customers with a Ghana contact address will receive a compliant invoice with required SDC information.  This applies to all B2B and B2C transactions, and all versions of the receipt (emailed, in-app and PDF). See example in the :thread:

:analytics-graph: *Impact & metrics:*
Compliance is revenue protective:
• *Penalties* are set at 65% of sales or *$324K* across QBO + MC:not-today-satan: 
• Ghana 2025 sales was *$188k ARR* w/*20% YoY growth* :chart-increasing: 
:dream_team: *Launched by:* Mailchimp Monetization *FINOPS* Squad
:clapping-all: *Shout outs:* <@U07SM68NTBL|Jonathan Robinson> <@U06GM26KU3U|Keerthi Joseph> <@U02KMFA7R2N|Ryan Simpson> <@W01BKFS7N8P|Navreet Kaur> <@U08DG6TKGGP|Patrick Khoo>
Thread: 7 replies (latest: 2026-03-16 06:30:05 PDT)
Reactions: celebrate-inclusive (10), rocket (6), praisethesun (1)



---

=== Message from Midori Chikamatsu (U09MBAJRP45) at 2026-03-11 08:53:39 PDT === 
Message TS: 1773244419.400799
:rocket-party:  *Launched | Automatically update C2s from QBO in MC* :rocket-party:

*What did we launch?*
C2 customers in QBO will be automatically added or updated in Mailchimp in their relevant audience.

This includes:
• New contact made a payment automations trigger, email and SMS templates, and associated merge content
• New contact's invoice changes state automations trigger, email and SMS templates, and associated merge content
Under the hood, this is powered by Mailchimp's new QuickBooks integration. We’re retiring the legacy Databridge and moving to the new pipeline, which is what allows more robust activations while preserving the subscription-status nuance we need. That same foundation will unlock additional use cases on top in a scalable way going forward.

We launched this as an A/B test to measure and monitor overall impact before scaling. The main UI change is in the QB Bundles flow (the onboarding steps between QBO and Mailchimp) where we removed the marketing consent step for the treatment group since this step used to bucket all C2s into either “subscribed” or “unsubscribed” groups. With this new launch, we are preserving the nuance of each C2’s subscription status and enabling more seamless automation triggers tied to payment and invoice state changes.

Although this was launched as an A/B test, the work to get here included a lot of teams and significant effort. Thank you everyone who contributed to making this happen!

If I missed anyone, please let me know and I will add them.

Automations: <@U06QWR7FV9T|Elizabeth Bertasi>   <@U09BAMA1N9X|Nakul Lahoti> <@U03GVFDGUKA|Cliff Martin> <@U02KMGM5D98|Yena Ku (they-them)> <@U02KJ1UDHC5|Bobby Craig> <@U03GE2Y59M0|Dana Winn (Automations Oncall)> <@U02KZU660AV|Jameson Brown> <@U02KMC0QGSW|Justin E. Samuels> <@U07UCSZSA30|Keith Ferney> <@U02KMDU1TU2|Maxwell Reich> <@U07NA0QPYJ0|Saisharath Peddibotla><@U07UY6KBVNV|Rob Berryhill> <@U09LKQLTUF4|Swati Pawar> <@U09RVPBJE1G|Alex Gutierrez> <@U02P9STSQGZ|Becca Walsh> <@U02KZMX4E6M|Celeste Mora (they/them)> <@U02KMBDS7AP|Heather Dartz> <@U02KJBP43V3|Jess Riddle (She/Her)> <@U02KJ5X1V3P|Cary Duncan> <@U07RKQ1P8Q2|Yizhou Qiu>
SMS: <@U02KPE15PCL|Connor Callahan> <@U02KJEHK677|Neil Desai> <@U03NU55364D|Satish Sambandham> <@U04QZ1RRPLN|Ty Kuhn> <@U0946BZ3QTW|Mike O'Dell> <@U03V70QRTRQ|Mythili Gopikanth> <@U07T1UYE259|Rick Barker> <@U0703THQZRQ|Gary Aloisio> <@U03J3GGU5T3|Jeremey Nofzinger> <@U09PS80BY85|Mesam Haider> <@U03TDLSFYH0|Ben Marks> <@U044UN28H6C|Sreeram Jayan><@U076PQ83WPJ|Ana Bell>
Email: <@U09979JPH37|Ose Amiegheme> <@U03TC2MB06M|James Arama> <@U04SYBP56JZ|Michelle Ducote> <@U02KJE9JALV|Michael Hawkins> <@U02KJA0C137|Erin McCue> <@U02K6LEHGKZ|JB Lovell>
IDI Platform: <@U09A9P01S4F|Nick Triscritti> <@U07U1NNUHRC|JP McConnell> <@U03TDGU2JUB|Josh Day>
QB Product Growth: <@U08Q4H23Y6P|Jay Shah> <@U06UFM02AAD|Jasmeen Sran> <@U022E60BE5U|Yen Phoaw> <@W90QBDG1L|Yashwanth Musiboyina>
MC Product Growth: <@U03UER0JRMY|Scott Stewart>
Thread: 6 replies (latest: 2026-03-11 17:58:13 PDT)
Reactions: white_check_mark (8), humongous-slay (9), woohooo (8), tada (19), raised_hands (9), raised_hands::skin-tone-2 (2), raised_hands::skin-tone-4 (1)



---

=== Message from Lucas Ruprecht (U09FQRBQSRF) at 2026-03-13 08:00:02 PDT === 
Message TS: 1773414002.074699
:rocket_launching: *Launched | Mailchimp Account Sandbox (Experiment x250) to 100%* :rocket_launching:

*What did we launch?*
We’ve launched the experiment for *Mailchimp Account Sandbox* - a fully isolated, production-safe environment where customers can explore advanced Mailchimp capabilities without risking their real data.

The Sandbox behaves like a full Mailchimp account and comes pre-populated with:
• 1,000 realistic synthetic contacts (single audience) with tags, engagement history, and ecommerce attributes
• A connected dummy Shopify-style store with products, variants, and order history
• Sample campaigns with representative performance metrics
• Pre-built automations (e.g., abandoned cart, SMS journeys)
• Premium-tier feature access for testing (no billing impact)
Sending is fully disabled at both the UI and backend layers, ensuring no real emails or SMS can be sent. The environment is visually distinct, fully isolated from production, and automatically expires after 30 days to keep data lightweight and compliant.

*Why this matters*
Today, Mailchimp forces all configuration and testing directly in production, leading to user anxiety, accidental sends, misconfigured journeys, corrupted lists, and avoidable support burden.

Over 300k customers maintain both a free and paid account just to test safely, a strong signal that users want a safe environment to explore. Sandbox addresses this head-on by:
• Removing the psychological barrier to trying advanced features
• Creating a repeatable, resettable onboarding and training environment
• Establishing a foundation for future capabilities like synthetic event generation, automation simulation, and test-mode integrations
The value of providing this natively is validated: when QuickBooks introduced a sandbox for trial customers, it generated +4k GNS per year and *$4M in annual revenue lift* (<https://docs.google.com/document/d/1seu1fKBn46L-IoUSNTd0Ui2LwKXldYPL_sh4bZsW5rU/edit?tab=t.0#heading=h.pub2youg77gg|QBO sandbox analysis>). Mailchimp lacks an equivalent environment today despite sandboxes being an industry standard in mature SaaS platforms (e.g., HubSpot, Shopify etc).

*Under the hood*
Sandbox leverages our existing Demo Account infrastructure (DemoAccountManager, AdminApi DemoAccountService, and Cloud Tasks job chain) to provision fully populated environments with minimal incremental engineering.

This experiment helps us validate provisioning reliability, creation time, usage depth, and impact on support volume before broader rollout.

While this initial launch is just scratching the surface of the possible benefits that Sandboxes can provide to new Mailchimp users, it was a massive undertaking involving dozens of people across the org. <@U08Q4H23Y6P|Jay Shah> deserves immense credit for driving this effort (and the QBO Sandbox work that preceded it!) forward from day one, working through concerns from engineering leadership and driving alignment on a technically complex offering on a tight timeline.

Beyond Jay, huge props to the whole team involved in this launch: <@U02L01PG77B|Marcus Judd>, <@U02L02R0Z97|Nic Cannington>, <@U02KJBAQMRT|Jaavan Greene>, <@W8FL2R1J6|Roopesh Sheth>, <@U02LPKLM222|Benji Adams>, <@U02KZMDS9UZ|Alyshah Ebrahim (they/them)>, <@U02KEKNRQ4W|Kateryna Smal>, <@U03777BQK0B|Elaine Xue>, <@U02LANSE472|Alex Goncalves>, <@U08D0C42PJM|Andrew Spitz>, <@U07TMNHQ20N|Phuong Trang>, <@U02KMCXQJ7M|Kelly Hale>

Identity PD - <@W8F4XD9U1|Arun Avanathan>, <@U02KEQF9LVC|Ticean Bennett> <@U06A00N0DG8|Ketan Barve>
MC PD/ICs - <@W8FL3AFU2|Amit Agrawal> <@U02KJ3JPUJ1|Alex Lehner> <@U02CJJ8MM6G|Kim Gurvitz> <@U02LAV5UQQ0|Blair Sullivan> <@U081BJXQFAR|Muthuselvam Chandramohan> <@U07B02LLNAC|Dmitri Medvedev> <@U02KP74TMT6|Brian Holbrook>
Leadership - <@U02KJG17Q0M|Tanisha Barnett> <@U06K8UTTSJE|Jing Wang> <@U07AX5J7MFB|Eric Anderson> <@U02K6NWDM7H|Marlene Mayfield>
Thread: 19 replies (latest: 2026-03-18 04:26:55 PDT)
Reactions: raised_hands (19), rocket (19), raised_hands::skin-tone-2 (3), party-woohoo (8), yay (3), sandbox (2), eyes (2), raised_hands::skin-tone-4 (4), raised_hands::skin-tone-3 (2), fire4 (2)
Files: Exp-Analysis: Trials Sandbox (ID: F0A20EPFMBN, application/vnd.google-apps.document, 0 Bytes)



---

=== Message from Jacquelyn Horgan (U02KMAN6V1R) at 2026-03-17 06:00:17 PDT === 
Message TS: 1773752417.295139
:rocket: *Nonprofit Discount Validation for US Customers* :money-bag:

:question-ids: *Background:* 
Mailchimp offers a 15% nonprofit discount on all Marketing plans to US customers who are exempt from Federal Income Tax.

:ugh: *Customer Problem:* 
Obtaining this discount isn't easy, and _it delays user first booking._ Customers have to search for it in <http://mailchimp.com/help|mailchimp.com/help>; redirect to a contact form, submit an inquiry, respond to an autoresponder, upload documentation via another portal, email back to let us know you've finished your upload, and then there's continued back and forth. It's time intensive for the customer and our Billing Care team, who manages 1K+ requests/year.

But wait, don't we want to make it hard for customers to get the discount?...

:analytics-graph: *Why it matters:* 
Nonprofit ICPs are an ideal user from a <https://docs.google.com/presentation/d/1C8a2H49Li7U0pJ7RFw5t6azt8JNVzG9C1v6DLjUSvCQ/edit?slide=id.g37bc8e834b3_0_240#slide=id.g37bc8e834b3_0_240|revenue perspective> - they pay more and stay longer. Compared to the general population they have:
*+37pt new bookings 12 month retention* 
*+18pt* overall retention
*+9 pt* NRR
*+10pt* GRR
Reducing friction for this segment directly supports long-term revenue growth and retention.

:search-pin: *What's new?*
We've taken the first step to automate this process by leveraging Intuit platform capability owned by the Know Your Business (KYB) team.

:trophy: *Result:* 
Billing Care can validate a C1s Nonprofit Status within 1 click in MCAdmin. This dramatically simplifies internal workflows and lays the foundation for customer-facing automation.

:yes-chef2: *What's next:*
• Strategically surface in-app, so customers can apply and receive the 15% discount in 1 click :approve: 
    ◦ We'll target our ICP at onboarding and over paid plan lifecycle, including churn flows. 
• Get more fish. :fish: 
    ◦ With automation, scale is no longer an issue. There's a massive opportunity to turn this into a marketing campaign to take priority position in the market.
    ◦ Think: :glitterstars: _*Mailchimp - How Nonprofits get more done*_:glitterstars: 
:dream_team: Huge thanks to the cross-functional team that brought this to life!
PD:
• Finops: <@U04623EPG8H|Hunter Ray> <@W01BKFS7N8P|Navreet Kaur> <@U047HMUGE82|Erin Szarpa> 
• KYB: <@W8FL2UEH0|Faraz Sharafi> <@W8FJ0JHMH|Huseni Kathiria> 
PM: <@U02KMAN6V1R|Jacquelyn Horgan> <@W8FMCGAVA|Guillaume Leger>
FARM: <@U032GEW7U0Y|Brent Hallinger>
Leadership: <@U07MYEG53JB|Rhomaro Tesfai-Powell> <@U02V0Q6K27P|Yilmaz Kara> <@U02KJAPC277|Glenn Branscomb>
Thread: 4 replies (latest: 2026-03-18 10:54:29 PDT)
Reactions: celebrate-inclusive (13), heart (12), clapclap (8), yellow_heart (8), awesome (2)



---

=== Message from Spencer Adkins (U02PW3SLJPJ) at 2026-03-17 14:12:38 PDT === 
Message TS: 1773781958.867289
:rocket::mailchimp: :money-bag: *Launched: Mailchimp ROI Calculator <https://mailchimp.com/resources/email-marketing-roi-calculator/|Webpage> & Impact Report* :rocket::mailchimp: :money-bag:
*We are officially LIVE with the <https://mailchimp.com/resources/email-marketing-roi-calculator/|Mailchimp ROI calculator webpage> and "The Roadmap to Marketing ROI" report!*

:goal:*The Strategy:*
• *Summary*
    ◦ As a critical step in the mid-market buying journey, prospects assess the potential ROI of marketing automation providers. Competitors like HubSpot and Klaviyo validate their value through public ROI calculators, previously placing Mailchimp at a disadvantage during the evaluation phase. *On 3/17, we officially launched Mailchimp’s first global ROI calculator to close this gap & highlight Mailchimp's value to mid-market business evaluating marketing automations providers.* 
• *Job to be done & target* 
    ◦ *GET* Mid-market prospects 
    ◦ *WHO* are currently evaluating or using competitive ESPs (HubSpot, Klaviyo, etc.)
    ◦ *TO* include Mailchimp in their consideration set and ultimately switch platforms
    ◦ *BY* validating the specific ROI and business impact they can expect (Revenue + Efficiency)
    ◦ *WITH* the promotion of a data-backed ROI calculator and accompanying impact report (produced in partnership with UserEvidence) that lives directly on our website 
:checkgreen: *What’s Next:*
• Campaign driving traffic to <https://mailchimp.com/resources/email-marketing-roi-calculator/|ROI calculator> launching March 19th (beginning with organic social followed by paid media) 
• March 27: initial read-out on modules test (outside of dedicated landing page, ROI calc modules have been placed on various web pages to test impact of ROI calc)
• April 7: three week post-launch read-out
:pray: *Special thanks to the team that made this possible!*
• PMO - <@U02LAM8RFTJ|Adam Batsakis> 
• ABM - <@U03J6V475DM|Erik van Os>, <@U08RML55YP7|Briona Brooks> 
• Web - <@U02B9R7MAH3|Brian Nguyen>, <@U0A6L7CA943|Linsey Fox> 
• SEO - <@U02KM9A5875|Chris Homer> 
• Organic Social - <@U02KJEMN6CD|Nicole Powell> 
• Paid Media - <@U03CE3UJVC0|Nicole Shroyer>, <@U02L0452RS5|Terrence Tucker> 
• Intuition - <@U02KJ3JLCS1|Brandon Krutzky>, <@U04DT14L0UX|Gray Chapman>, <@U02KMH7V2HH|Zemoria>, <@U02K6Q71FL7|ross zietz>, <@U02KPB904MA|Alyson West> 
• Legal - <@U02KENZHH6J|Robyn Taylor>, <@U07Q0RN0C5S|Renee Moore> 
• Dev - <@U02URC9KK46|Lawrence Ma> 
• PM - <@U03AQ35Q2P6|Franco Reyes> 
• PMM - <@U02KMH2SL83|Yesica Ford>, <@U02EYMLPS56|Steph Foust>, <@U02PW3SLJPJ|Spencer Adkins> 
Thread: 9 replies (latest: 2026-03-19 05:59:58 PDT)
Reactions: celebrate (15), amazing45 (9), nice-neon (4), party-cat (6)



---

=== Message from Stephen Yu (U040C49798T) at 2026-03-18 09:22:51 PDT === 
Message TS: 1773850971.062569
:rocket_launching: *LAUNCHED: Analytics Agent V2/Beta* :rocket_launching:
We are on a journey to *transform fragmented marketing data into clear insights and actionable recommendations through AI-native conversational experiences.* Through this work, we are evolving from passive, static reporting into proactive intelligence that guides users to optimize marketing performance. *What we have observed to date -* We launched Analytics Agent V1 earlier in the year with <https://intuit-teams.slack.com/archives/C03TLJNADSP/p1772468019988369|clear signals of product market fit>:
• +6% lift to email campaigns sent per user with directional improvement to churn reduction and attributed revenue 
• 80%+ engagement when users discovered the feature 
• 3000+ insights generated to date for users 
• Strong qualitative customer feedback with customers consistently highlighting the response quality and depth as a positive
        ▪︎ _"The AI gives me a depth of intelligence and analytics that is eye opening. Plus it summarizes without me having to go in and do it myself."_ 
        ▪︎ _"The responses were in depth and synthesized the data for me clearly."_
        ▪︎ _"The information that it is providing is really valuable and it would take a ton of time to come up with this information and the suggestions on my own."_
*This week, we launched Analytics AI (Analytics Agent) into Beta - a meaningful milestone in our journey. This builds on the strong momentum from our V1 launch, delivering a durable platform with enhanced eval and user experience.*

:customerproblem: *Customer problem:*
Today, businesses are heavily time-constrained and often lack the marketing expertise to maximize their performance. They spend hours manually analyzing data - 53% of SMBs immediately investigate unusual performance and 38% dedicate weekly time to analyzing campaigns. They are looking for solutions to uncover marketing opportunities and free up time to focus on what matters - growing their business.

:rocket4:*What was launched?*
We improved on the V1 version across multiple dimensions designed for scalability:
• Built on durable and performant data platform on CDP / StarRocks with a single source of truth for all of reporting & analytics 
• Expanded data coverage (SMS, Ecomm Activity, Product-level insights, contact activity)
• Enhanced data understanding layer with improved agent eval scores. Improved query accuracy score from 80%+ to 90%+
• Improved user context with C1 profile info 
• Enhanced user experience with streaming, conversation history and data visualizations leveraging GenUX components 
Who is this available for: Global paid MC users with recent campaign activity

Resource: <https://www.figma.com/design/wfGlMExf1rxooLDPwh98dd/Analytics-AI-Agent?node-id=3030-33438&p=f&t=FydIiTXa1rPhidxz-0|Design>, <https://docs.google.com/document/d/1nCu8TO8nOpYNvejX--GR-GMwL7YlhFhXk8zortznEdc/edit?tab=t.0|Test plan>, <https://docs.google.com/document/d/1CPbBTBLcpbRg827JI16WBhXVj-BB026t-jAgLYcdCyI/edit?tab=t.e56pbh3zhxyg|PRD>

:chart_with_upwards_trend: *Success Metrics*
• Increase in insight to action leading to completion of high value actions such as campaigns sent and connect integrations
• Increase in % of MC attributed revenue 
• Increase in R&A adoption 
• Agent eval: Online & offline evaluation of conversation quality 
:next: *What’s next?*
*Our goal is to become the marketing intelligence layer for how MC users understand and grow their business.* We are working towards getting to GA first in Mailchimp by continuing to iterate and improve on the end-to-end experience. We are also evaluating expansion to other surfaces to meet users where they are through Omni integration. In addition, we will proactively surface embedded AI-powered insights contextually within product surfaces so we can always lead with dynamic and personalized experiences. This involves closing the loop from insight to actions so we are showing users not just insights and recommendations but also done-for-you actions that further reduce manual work.

:megaphoner-1707: *Shout outs & HUGE THANKS*
*Thank you to the incredible team that has made this possible.* This required deep collaboration across many teams to deliver on customer benefits and innovation!

Engineering: <@U0428EDN518|Nick Boyle> <@U03EEL3PU9H|Sid Kumar> <@U09Q9KFSP8W|Jason Dudley> <@U01J5GVP5GV|Kuntal Naphade> <@W8FMAA7S8|Yi Zhang><@U02K6PD6HN3|Michael Heard> <@U07B02LLNAC|Dmitri Medvedev> <@W01108SHDV4|Sarvesh Kumar>
AI science: <@U02KM30QU10|Ben Leathers> <@U07SEHWU9AN|Nithali Sridhar> <@U0793KXBF51|Bryan Smith>
Design: <@U02KJ9QRSDT|Eddie Shrake> <@U0372SDKQDS|Tiffany Huang>
Product: <@U040C49798T|Stephen Yu>
TPM: <@W8GG78R1C|David McDonald>
Data Science: <@U07ED705DHS|Aastha Sehgal> <@U0970UUFN80|Ashish Prakash> <@U03BZL23C1F|Heuisu Kim> <@U091QJQCRMZ|Yiwen Yan>
Product Marketing: <@U03HRFYTYUB|Simone Kovacs> <@U096DLJK8NA|Jonathan Rodgers>
CDP: <@U04QNS5KEE6|Ajeet Seenivasan> <@U078B7PT3A8|Dan Damkoehler>
GenUX: <@U06QCEDF6KD|Abasifreke James> <@U08UHV16FMK|Theo Joseph>
LCPO: <@U02KENZHH6J|Robyn Taylor>
UXR: <@U02K6PV38NT|Rob Adair>
cc <@W8FHXCZSP|Saikat Mukherjee> <@W8FL6URHQ|Deepak Prabhakaran> <@U03EEL3PU9H|Sid Kumar> <@U02KPGZ4HHS|Jane Guthrie> <@U0970UUFN80|Ashish Prakash> <@U09QF7F45AQ|Nathan Snell>
Thread: 16 replies (latest: 2026-04-28 13:04:31 PDT)
Reactions: rocket (21), awesome-star (11), clapclap (8), thankyou1 (3)
Files: Screen Recording 2026-03-18 at 12.16.28 PM.mov (ID: F0AME9BERD0, video/quicktime, 80.7 MB)



---

=== Message from Connor Callahan (U02KPE15PCL) at 2026-03-19 11:00:17 PDT === 
Message TS: 1773943217.854029
:rocket: :landed2: *Launched and Landed | Recommend SMS After Import to Prospects | <https://docs.google.com/document/d/1ek7a3JpjoN2NsCk_IqvSq8i0B4XtI3gn3Ga6TEOpo0U/edit?tab=t.0|EDD>* 

The *SMS Growth team*, in collaboration with our *Audience Partners*, is excited to share a winning experiment from the SMS growth lineup.

:test_tube: *Problem & Hypothesis:* 130k+ paid Mailchimp users import contacts every month. For 50% of them, they have to wait while contacts are processed. For 97% of these users, SMS isn't enabled, even when the contacts they're importing include phone numbers. We hypothesized, and our DS Propensity Model confirmed, that by detecting the presence of a phone number field and surfacing an SMS recommendation _while users waited for their import to complete_, we could make SMS feel like the logical next step, not a separate product to go find on their own, ultimately increasing the purchase rate of SMS.

:boom: *Impact*
• :updates: *FY27: $495K in incremental SMS revenue*
• :updates: *+5bps SMS penetration in FY26 ($90k)*
• :updates: *+807 net new SMS bookings in FY26*
• :updates: *+33%* increase in SMS Purchase Rate
• Email send rate held _flat_ - zero cannibalization of core email behavior :white_check_mark:
:product-insights: *What's Next:* 
    ◦ *Lifecycle follow-up:* Invest in re-engaging users who saw the prompt but didn't act, an untapped audience already primed.
    ◦ *Multi-audience & multi-country detection:* Expand phone number detection to cover users with contacts in countries where they haven't setup SMS yet.
    ◦ *Lifecycle marketing integration:* Connect this signal to downstream nurture flows for users who started but didn't complete SMS registration
:extreme-teamwork: *Dreamwork Merits Celebration*
A huge thank you to the SMS Growth team, Irrational Labs and Audience partners:
• SMS Growth
    ◦ SMS Growth Eng: <@U098480GM26|Minal Rivonker> <@U09LGAM2PHT|Arpit Parekh> <@U02KMCXQJ7M|Kelly Hale> <@U0A3P6A30PN|Ekaterina Makarova> <@U0A3Z9B8XPX|Meenakshi Arya> 
    ◦ Design: <@U02KM1TUH8B|Ashley Lawrence> <@U02KJF76MU5|Rujuta Apte> 
    ◦ Irrational Labs: <@U05DS9303MX|Jeff Ott> <@U09LXPTCQSG|Harrison Neuert> 
    ◦ TPM: <@U076PQ83WPJ|Ana Bell> 
    ◦ DS: <@U0970UUFN80|Ashish Prakash> <@U02724E1DFB|Jeremy Diaz> <@U06UQL9V07R|Himanshu Dubey> 
    ◦ Product: <@U02KPE15PCL|Connor Callahan> <@U02KJEHK677|Neil Desai> 
• Audience: <@U091MQW7VUP|Kyle Jones> <@W012EU6L7FG|Payton Camilli> <@W019Y5V05UG|Mohammad Habbab> <@U07USKD0MA5|Shefali Dalal> 
Thread: 1 replies (latest: 2026-03-19 15:32:52 PDT)
Reactions: blob-tada (15), rocket (13), wow-frog (4), yay (1), raised_hands (1)
Files: Screen Recording 2026-03-18 at 1.12.43 PM.gif (ID: F0AMHB3HD35, image/gif, 2.4 MB)



---

=== Message from Chelsea Youmans (U02KJ63H57X) at 2026-03-19 13:28:55 PDT === 
Message TS: 1773952135.735879
:rocket: *Mailchimp Mobile Update: Email Editing Agent on Android* :android: 

:dart: *Context & Overview*
Mailchimp customers send approximately *38K Nuni emails from the Mobile App every week*. However, editing email campaigns on mobile can be frustrating. Smaller screen sizes limit visibility, certain editing features are harder to access, and navigating controls can be time-consuming.
To address this, we introduced the *Email Editing Agent* — a conversational AI experience that enables users to update their campaigns using natural language. Instead of hunting for controls, customers simply describe what they want to change, making mobile editing faster, simpler, and more intuitive.

:bust_in_silhouette: *Customer Problem*
*I am* a small business owner using the Mailchimp Mobile app to manage my audience and campaigns.
*I am trying to* make quick edits before sending an email to my customers.
*But* I can’t easily find the controls, and it takes too much time.
*Because* limited screen space means options are hidden, missing, or difficult to navigate.
*Which makes me feel* frustrated and less confident in the email I’m about to send.

:bulb: *Hypothesis*
We believe that enabling users to describe their desired edits in plain language will:
• Reduce the time it takes to make campaign updates
• Simplify the mobile editing experience
• Increase user confidence before hitting “Send”
:rocket: *What We Launched*
We launched the *Mailchimp Email Editing Agent* on Android _(iOS coming soon)_.
With a built-in chat experience, users can instruct the AI agent to make both simple and complex edits. You can ask it all sorts of things, such as:
• Are my social links set up right?
• Translate everything into Dutch.
• What do you recommend I change?
• Apply a Mardi Gras theme, please!
• Make the third paragraph shorter.
Instead of navigating menus, users just say what they want — and the agent takes care of the rest.
*Download the Mailchimp Android app to try it today!*

:triangular_ruler: *Design reference:*
<https://www.figma.com/design/BfLb1Qo8FNvQmZqwRlP3ov/Nuni-AI-Editing?m=auto&t=mKrqp2U0KYNDfNQN-6|Figma — Nuni AI Editing>

:bar_chart: *Early Results:*
Since launch on Android on Tuesday, March 3rd, we've seen:
• 35 users have interacted with the agent *280 times* :chat-pinkheart: 
• *57% of those users continued to send campaigns* :paperplane: 
_*Up next...*_
• Release on iOS
• New image editing tooling
• Improved Nuni doc validation
:raised_hands: *Shoutouts & Thanks*
Huge thanks to the design and engineering teams for pushing this forward.
MC Mobile Eng: <@U02KMGACC90|Tamer Barsbay> <@U02KMFMLW59|Phiet Do> <@U02KJ63H57X|Chelsea Youmans> <@U02KEM59CCW|Mark Abdelmalak> <@U06L6KAUA30|Julian Fordyce> <@U02KEHZ4PHC|Gaby Chacon> <@U02LB5Y9XG8|Shawn Veader> <@U02KJF2PPUM|Sal Aparo>
AI Science: <@U0651FGUYN9|Ian Maffett> <@U064FLW0QAK|Taylor Horton> <@U0793KXBF51|Bryan Smith> <@U088EJ0JL5C|Sri Kambhammettu>
Core Email: <@U06GTAA3E8G|Justin Little>
MC Mobile Design: <@U02KPCDC752|Aparna Somvanshi>
Reactions: woo_hoo (17), mobile-frenz (12), mobile-love (8), intuit-assist-thinking-1665 (4), nice_ (6), raised_hands (1), raised_hands::skin-tone-6 (1)
Files: 1647.mp4 (ID: F0ANK2E14AC, video/mp4, 17.6 MB)



---

=== Message from Connor Callahan (U02KPE15PCL) at 2026-03-20 05:02:00 PDT === 
Message TS: 1774008120.314429
:rocket: :landed2: *Launched and Landed | Recommend SMS to C1s with C2 Phone Numbers in Audience*

The SMS Growth team and Audience are back with *another winning revenue driver.* 

:test_tube: *Problem & Hypothesis:* Our <https://docs.google.com/presentation/d/1kWXplLOg2imWaF96H1xeA8iQVkaCJ9RPHM_VHR-az2w/edit?slide=id.p2#slide=id.p2|DS Propensity Model> identified that having a phone number for 60%+ of contacts is the 2nd highest predictor of SMS purchase. Yet most users navigating to the all contacts page never see a reason to sign up for SMS. We hypothesized that by surfacing a personalized, contextually relevant SMS recommendation directly on the Audience page (e.g. _"60% of these contacts have phone numbers. Use SMS to get better performance out of your marketing."_), users would treat SMS registration as a natural part of their audience management workflow, not a separate product to go find on their own.

:boom: *Experiment Impact*
• :updates:  _$230k FY26_
• :updates:  _$1.2M FY27_ 
• :updates: _2,000+ net new SMS bookings in FY26_ (+13 bps in FY26 and +19 bps in FY27)
• :updates: _+38%_ increase in SMS Purchase Rate
• Audience import completion rate held _flat_ - no cannibalization of core audience management behavior :white_check_mark:
:boom: *Cumulative SMS Growth Impact (Past six experiments including this one)* 
• :updates: 6 winning experiments expected to drive *9300+* bookings in FY26
• :updates: +45 bps to SMS penetration
• :updates: $1.08M FY26 
• :updates: $3.96M FY27 
:product-insights: *Insight & Next Steps*
•  We tested three different variations of the primary CTA and were surprised by the results.
    ◦ "Register for SMS" +37.9% (most explicit about effort) - winner 
    ◦ "Continue" +19.6% (ambiguous)
    ◦ "Turn on SMS" +11.5% (sounds quick/easy)
• Update the import confirmation from "Turn on SMS" to "Register for SMS" button label. (Potential 320% gain 11.5% -> 37.9%) 
• Test the winning primary call to action "Register for SMS" on our past winning experiments via x258 and x259.
:extreme-teamwork:  A huge thank you to the SMS Growth team and to our Irrational Labs and Audience partners:
• SMS Growth
    ◦ SMS Growth Eng: <@U098480GM26|Minal Rivonker> <@U09LGAM2PHT|Arpit Parekh> <@U02KMCXQJ7M|Kelly Hale> <@U0A3P6A30PN|Ekaterina Makarova> <@U0A3Z9B8XPX|Meenakshi Arya> 
    ◦ Design: <@U02KM1TUH8B|Ashley Lawrence> <@U02KJF76MU5|Rujuta Apte> 
    ◦ Irrational Labs: <@U05DS9303MX|Jeff Ott> <@U09LXPTCQSG|Harrison Neuert> 
    ◦ TPM: <@U076PQ83WPJ|Ana Bell> 
    ◦ DS: <@U0970UUFN80|Ashish Prakash> <@U02724E1DFB|Jeremy Diaz> <@U06UQL9V07R|Himanshu Dubey> <@U08CE9D9QKS|Patrick Kopps><@U02LB056SQ0|Essence Coleman> 
    ◦ Product: <@U02KPE15PCL|Connor Callahan> <@U02KJEHK677|Neil Desai> 
• Audience: <@U091MQW7VUP|Kyle Jones> <@W012EU6L7FG|Payton Camilli> <@W019Y5V05UG|Mohammad Habbab> <@U07USKD0MA5|Shefali Dalal>
<https://docs.google.com/document/d/1Pe09vb7aprJ5hmAvn5sdxlre6WOB4G4IPpve2XBH7Zk/edit?tab=t.0|x287 EDD>
Thread: 5 replies (latest: 2026-03-20 11:03:42 PDT)
Reactions: party-blob (26), clapping-all (16), dream-team- (9), rocket-party (10), raised_hands (2), raised_hands::skin-tone-2 (2), raised_hands::skin-tone-3 (1)



---

=== Message from Connor Callahan (U02KPE15PCL) at 2026-03-20 09:32:22 PDT === 
Message TS: 1774024342.869049
The experience curtesy of <@U02KM1TUH8B|Ashley Lawrence>!
Reactions: hearts (1)
Files: x.gif (ID: F0ANR30QGV6, image/gif, 3.8 MB)



---

=== Message from Devin Mercier (he/him) (W0132PNAC9X) at 2026-03-20 10:12:31 PDT === 
Message TS: 1774026751.825339
:whatsapp-rocket: *LAUNCHED: WhatsApp Private Beta* :whatsapp-rocket:
The numbers here are hard to ignore. WhatsApp has *3 billion monthly active users* and *2.3 billion daily active users* worldwide. It's the most popular messaging app in over 100 countries, used by 38% of the global population and 69% of all internet users (excluding China). Our own internal CMI research confirmed the desire for WhatsApp: 87% of business users cite promotional messaging as a top WhatsApp use case, and in Europe alone, 52% of messaging intenders plan to adopt WhatsApp as their primary channel.

WhatsApp is essential to Mailchimp's evolution as an omnichannel marketing platform. As we develop our Acquisition Agent and broader automation capabilities, every major channel where customers connect—including WhatsApp—needs to be tightly integrated. Without WhatsApp in our channel mix, our automation tools and global reach would fall short in key markets where it is the dominant business communication platform. Expanding to WhatsApp is central to building a truly holistic, global marketing experience for our customers.

We launched WhatsApp Private Beta on March 11 with a cohort of up to 20 CSM-managed customers. This is a constrained, intentional beta: we're trading scale for deep learning before we expand to 100 customers in April.

:customerproblem: *Customer problem:*
*I AM* a marketer trying to reach customers through multiple marketing channels
*I AM TRYING TO* run a coordinated strategy across email, messaging, and every channel my customers actually use -- so my marketing feels cohesive, not scattered
*BUT* my tools are siloed: email lives in one platform, SMS in another, and channels like WhatsApp require a separate setup entirely
*BECAUSE* building a true omnichannel presence requires integrating tools, managing multiple platforms, and a level of technical coordination most small businesses can't sustain
*WHICH MAKES ME FEEL* like I'm running disconnected campaigns instead of a real marketing strategy, while my customers experience something fragmented

:whatsapp-rocket-intensifies: *What was launched?*
WhatsApp is now live inside Mailchimp for our first cohort of beta customers. It's a first-class channel sitting alongside other Mailchimp channel -- no new platform to learn. Check out the Figma <https://www.figma.com/design/RXnlSAUVvGcRT7T7SW5TfM/WA--WhatsApp-Extended-Private-Beta?node-id=7-276402&t=NDlq3KeLtq0sl5Rj-4|here>.

*What beta customers can do today:*
• *Set up WhatsApp for their business*: Connect their WhatsApp Business Account through our embedded onboarding flow
• *Create and send campaigns*: Build rich messages with images, buttons, merge tags, and AI-assisted copy in the same builder leveraged for RCS that they may already know
• *Two-way messaging via Inbox** Respond to subscriber replied via our mobile and in-app Inbox capabilities
• *Track performance*: Dedicated WhatsApp reporting specific to WhatsApp campaigns
*Coming soon:*
• Automations with Send WhatsApp functionality (April)
• Self-serve registration ramping to 100% (Public Beta target: July 2026)
:next: *What’s next?*
We're in week 2 of our private beta. We're tracking activation rates, campaign performance vs SMS, and credit purchase behavior. More onboarding calls are happening next week and the cohort is growing!

*Early Success Story* :star-struck:
Our first customer, *2four6*, completed onboarding last week and hey didn't just get set up -- they're already thinking about scale! They've expressed interest in signing up *7 more of their audiences* to WhatsApp and have committed to purchasing *30K additional messaging credits* to support the WhatsApp channel expansion! Shout out to <@U060NKPDHF1|Swati Bala Subramanian> and <@U087TFW2RMF|Sophia Lenik>'s sell here + increasing the MRR of this customer +$300 through messaging credit spend. We have an additional customer who has accepted our Beta terms and is ready to onboard as soon as Monday!

That's the kind of early signal we want to see in Week 1!  :whatsapp-deal-with-it:

:megaphoner-1707: *Shout outs & HUGE THANKS*
This took a massive cross-functional effort across more than a dozen teams. Genuinely grateful for every person on this list.

*Product*: <@W0132PNAC9X|Devin Mercier (he/him)> <@W013E2DDP3J|Alina Rainsford> <@U087ERCHR4P|Jorge-Luis Leon> <@W012EU6L7FG|Payton Camilli> <@U02KZSQSXAM|Curt Shearer> <@U02K6SAGNUX|Zack Wright> <@U06UL7W90LS|Vivian Wang> <@U02LB4JPAEL|Nicole Jayne> <@U086AEY40BF|Chethana V P> <@U02K6SAGNUX|Zack Wright> <@U04FF36UREJ|Lina Lozano Oviedo>

*Design*:<@U04RXGCEPCY|Tracie Kreiss> <@U03V70QRTRQ|Mythili Gopikanth> <@U02KMFKKDU2|Sahana Srivatsan> <@U06K1M3KGHZ|Laura Guillen> <@U080VTBGJ7N|Diane Hahn>

*Engineering (across 10+ teams!)*:
<@U03BN5DCNMT|Ruth Libowsky> <@U03J3GGU5T3|Jeremey Nofzinger> <@U0946BZ3QTW|Mike O'Dell> <@U07T1UYE259|Rick Barker> <@U03NU55364D|Satish Sambandham><@U02KMCPHWAX|Laura Celentano> <@U04QZ1RRPLN|Ty Kuhn> <@U02LANRD7R6|Adam vanWestrienen><@U044UN28H6C|Sreeram Jayan><@U02KJ9AN5FF|Christian Blades><@W0133SBDGCA|Chung (Chunghee) Kim><@U0996V08PQB|Krishna Gudimetta> <@U06QHNDKYQK|Leo Lin> <@U09B395N6D6|Allyson English> <@U07LPMM9HL6|Chintan Patel> <@U02KZSVL75F|Christina King> <@U05UYGBTQ3T|Nikki Panda> <@U045QK7AM1A|Anesia Smith> <@U047HMUGE82|Erin Szarpa> <@U02KM87A7SN|Brittany Tims> <@U02KZQ945CH|Carlton Freeman> <@U03FZ581XTR|George Nakkas> <@W019Y5V05UG|Mohammad Habbab> <@U09B1S1DZ6Y|Sundeep Nadendla> <@U03TAMKCM37|Patricia Blackwelder> <@U02VDDRRUG7|Stephen Tiedemann> <@U072K66P5CH|Samhitha Tummanapalli> <@W01108SHDV4|Sarvesh Kumar> <@U03EEL3PU9H|Sid Kumar> <@U06U846AJFJ|London Baker> <@WK626SJMC|Sudeepta Das> <@U03JKJV4RGR|Marcus Moncayo>  <@U02KMA7JMPV|Dev Sabharwal>  <@U06QZKUP142|Sean Fleming> <@U076PQ83WPJ|Ana Bell> <@U07PV9VL1HD|Omar Carrasco> <@U07USKD0MA5|Shefali Dalal> <@U02KJBP43V3|Jess Riddle (She/Her)> <@U03CJLQEUCF|Remya K> <@U07TBG84162|Andres Botero> <@U03TDLSFYH0|Ben Marks> <@U06D0QM9L1F|James Dominic> <@U09FE7Q8GRZ|Ivan Navarrete> <@U09GBP7QP32|Fernando Rodriguez> <@U06DNT6E69F|Swanand Patil> <@U09MSSM0GP3|Pascal Audant> <@U03PXS338NA|Mike Mannix> <@U04739FF7M5|Adam Williams> <@U09RWU1AAR2|Sivaram Ramalingam>

*Trust & Safety*: <@U056BR646S0|Aina Danilova> <@U02CJJ8MM6G|Kim Gurvitz> <@U08637A29EX|Hao Tan> <@U07BLPT6HGQ|Saranya Natarajan>

*Data Science*: <@U06UQL9V07R|Himanshu Dubey> <@U02724E1DFB|Jeremy Diaz>

*Data Engineering*: <@U02LAV55V40|DeAnna Rushing> <@U02KMCPUWEP|Emmett Bamford> <@U02KP74TMT6|Brian Holbrook> <@U02KEKMTNNA|Jenn Reed>

*GTM*: <@U096X02TTP0|Kendall Kautz> <@U060NKPDHF1|Swati Bala Subramanian> (first onboarding!), <@U037ZE99WC9|Madaline Goldstein> <@U07F2TB4Q1K|Sunali Bhandula> <@U08DFFPV215|Andrew Rodrigues Anes> <@U02LB0ECVR6|Eric Cash> <@U0AHB4JSV2L|Zach Claywell> <@U094GCV941F|James Panter> <@W8FMB5WKW|Barb Magner> <@U05QNVD0KHP|Cuc Le> <@U02K6K2FGDD|Frances Bethel> <@U02LB24A108|Kali Watson (she/her)> <@U0886F7RZBJ|Krunal Shah> <@U02TNUQ1868|Srinivas Manepalli>

*Leadership*: <@U08KK7S6LAZ|Diana Williams> <@W8FHYGK19|Jack Tam> <@W8FQBMAN9|Andrew Firstenberger> <@U02KJF76MU5|Rujuta Apte> <@U02KJEHK677|Neil Desai> <@U07AX5J7MFB|Eric Anderson> <@U0ACRAXEK7T|Mani Dhillon>
Thread: 14 replies (latest: 2026-03-25 09:37:27 PDT)
Reactions: whatsapp-deal-with-it (53), whatsapp-intensifies (43), party-blob (38), yay-frog (25), clapclap (28), dance_vibe (9), peanutbutterjellytime (8), whatsapp-rocket (1)



---

=== Message from Nicole Jayne (U02LB4JPAEL) at 2026-03-23 06:15:01 PDT === 
Message TS: 1774271701.629159
:reportingsquad: *Comparative Reports Transitions to Custom Reports* :sunset-1: 

Pour one out for Comparative Reports. Originally launched in 2015 with Mailchimp Pro, the tech powering this legacy feature officially reached the end of its lifecycle. This tool was increasingly left behind without the ability to report on bot-filtered opens/clicks or attributed revenue - leaving marketers in the dark about their true impact. _The last date for Comparative Reports was Thursday, March 19._

:rocket: *What was launched?*
This presented an opportunity to standardize all reporting on a single, CDP-backed tool: Custom Reports. While workflow changes are always challenging for time-strapped marketers, the plan ensures the smoothest possible transition for the long tenured 4,700 affected users valued at $2.2M MRR.

• Custom Reports was brought up to near-parity with Comparative Reports (segments coming soon!), and added to the legacy Pro add on plan
• ~4,700 Comparative Reports users had 2 years worth of reports _automatically migrated_ to Custom Reports
• Customer care to smooth the transition with in-app notices, lifecycle email, KB article and CSM/customer team enablement
:sad-customer: *Why is this customer obsessed?*
Mailchimp historically maintained two reporting tools with different data sources and capabilities. This created mismatched data between reporting surfaces, with confusion and slower time to market for new reporting features.

By retiring Comparative Reports and standardizing on Custom Reports, we are ensuring customers have the highest quality data with access to:
1. Bot filtered open and click data
2. A consistent source of truth powered by CDP
3. Conversion (orders, revenue) metrics 
4. Faster time to market for new channels and analytics features across a modernized stack (I see you Whatsapp)
:time_clock: *Why now?*
Significant cost savings: sunsetting Comparative Reports is a key piece of work contributing to $3M in infrastructure cost savings from ElasticSearch decommission.

:new-badge: *What changed?* 
From:
• Two separate reporting tools (Comparative + Custom)
• Data inconsistencies between tools
• No conversion metrics in Comparative Reports
• Legacy infrastructure limiting feature velocity

To:
• One standardized reporting tool (Custom Reports)
• Unified CDP-powered data across Analytics
• Ecommerce conversion metrics and bot filtering
• Reporting across email and SMS
• Faster feature rollout across a modernized system
:tape-measure: *How will we know this was successful?*
• Preservation of $2.2M MRR tied to migrating users
• Reduction in VOC related to data inconsistency
:next: *What’s next?*
R&A will add segment filtering to Custom Reports to close the last Comparative->Custom parity gap experienced by ~400 users. This also unlocks a larger, longstanding customer ask to analyze and export historic performance across segments of contacts (tag, signup source, custom fields, purchase history, etc!), driving discovery of valuable segments and informing future marketing plans.

:reportingsquad: All contributors here deserve the MVP award for their quick thinking, creative solutions, and get-it-done spirit:
Eng: <@W01108SHDV4|Sarvesh Kumar> <@U08CMPYH8TY|Freddy Giordano> <@U09E76WKB7B|Surendar Dharani> <@U09RBTL7F47|Praveen SB>
QA: <@U02LB056SQ0|Essence Coleman>
Design: <@U02KMFKKDU2|Sahana Srivatsan>
Product: <@U02LB4JPAEL|Nicole Jayne>
TPM: <@U0AKB0WCUTC|Nakib Khandaker>
Product Marketing: <@U096DLJK8NA|Jonathan Rodgers> _--> absolutely essential partner!_
Leads: <@W8FL6URHQ|Deepak Prabhakaran> <@U03EEL3PU9H|Sid Kumar> <@W8FHXCZSP|Saikat Mukherjee> <@U02KPGZ4HHS|Jane Guthrie>

And additional thanks to the PLC & Rev Rec teams for proactive actions to retain the 400 users experiencing a short term feature gap! <@U02KZSQSXAM|Curt Shearer> <@W8FMB5WKW|Barb Magner> <@U05QNVD0KHP|Cuc Le>
Reactions: pouroneout (8), clapclap (7), celebrate (5), rip (2), rt-launched (1), sunset-1 (1), heart (1)



---

=== Message from Ose Amiegheme (U09979JPH37) at 2026-03-31 09:00:05 PDT === 
Message TS: 1774972805.695499
*Launched and Landed | Nuni Sections Manager* :win:

Sections Manager is now rolled out to 100% of Nuni users following a clear experiment win. At full rollout, we expect it to drive ~845 additional weekly C1 senders, with an estimated ~$20k FY26 in-year revenue impact and ~$145k annualized revenue impact. It also establishes the foundation for Saved / Reusable Sections.

:boom: *<https://github.intuit.com/pages/Mailchimp-Analytics/product-analytics/experiment-readouts/section-manager-experiment-readout/|Experiment Impact:>*
:updates: ~845 additional weekly C1 senders expected at full rollout
:updates: ~$20k FY26 in-year revenue impact
:updates: ~$145k annualized revenue impact
:updates: Clear win on C1 send rate
:updates: Send volume and C2S also trended positive

:mag: *Customer Problem:*
Marketers build emails in meaningful chunks like headers, heroes, promos, product grids, and footers. But Nuni primarily exposed email structure through blocks and three fixed wrapper containers: Header, Body, and Footer. That made larger emails harder to organize, edit, and reason about, especially when making structural changes across the full message.

:rocket: *What Launched:*
Sections Manager introduces a dedicated sections experience in Nuni, including:
• A new Sections tab in the side panel
• A library of prebuilt sections that can be dragged into emails and templates
• Inline section controls on canvas to reorder, rename, duplicate, and delete sections directly
Together, these changes make structural editing easier and give users a clearer mental model for how to build and manage email content. See a demo recording <https://www.loom.com/share/3ca6b362c22644629fda650c93304147|here>.

:bulb: *Why It Won:*
Users think of emails in small modular chunks. By making Sections a first-class concept in Nuni, we reduced friction in structural editing and made the builder more intuitive for real customer workflows. That improvement appears to be translating into better sending outcomes, which is why we saw a clear win in the experiment.
We are also seeing encouraging qualitative validation since rollout. Customers and practitioners have been sharing positive feedback on Linkedin about the new Sections experience, especially the ability to manage content in clearer, more meaningful chunks. That unsolicited market reaction gives us additional confidence that this is solving a real customer pain point.

:footprints: *What’s Next:*
Sections Manager is now fully rolled out, and we’re building on that foundation with Saved / Reusable Sections (releasing 4/28).
We’ll continue monitoring:
• Send outcomes as adoption scales
• Section library engagement and usage patterns
• Follow-on usability improvements

:extreme-teamwork: Huge thank you to the team who made this happen
Design: <@U03C0H8SPPX|Christian Vadi>
Engineering: <@U02KJ3E3M53|Alex Wilson [email oncall]> <@U02KM1QA89Y|Adam Verwymeren> <@U05UF6MQK0D|Annie Kong> <@U02LB4SBY0Y|Paul Lee> <@U02KMDVUEUT|Mike Murray>
Data: <@U02QFTEHKB9|Kevin Martin>
Product: <@U09979JPH37|Ose Amiegheme>
UXR: <@U02KM6ZMJ8J|Bethany McDaniel>
TPM: <@U02LB3HSDRN|Marissa Rivera>
Leads: <@U02KJA0C137|Erin McCue> <@U02K6LEHGKZ|JB Lovell> <@U02KJE9JALV|Michael Hawkins> <@U07AX5J7MFB|Eric Anderson>
Thread: 5 replies (latest: 2026-04-01 09:27:06 PDT)
Reactions: yay-frog (25), party-dino (10), celebrate-dance (7), party_rocket (9), peanutbutterjellytime (6), lets_go (5), nice-neon (2)
Files: image (1).png (ID: F0APVKTUE58, image/png, 55.7 KB), IMG_7571 (1).png (ID: F0APP8EC4EP, image/png, 418.5 KB), Screenshot 2026-03-19 at 9.39.13 AM.png (ID: F0APE6HATFZ, image/png, 198.2 KB)



---

=== Message from Alex Wilson [email oncall] (U02KJ3E3M53) at 2026-03-31 10:52:28 PDT === 
Message TS: 1774979548.052319
Users have been asking for this for _years_—even before I joined 12 years ago :scream_cat:
Really proud of this team. The level of thought and intention that went into this work truly shows, and our users are already feeling the impact.
This goes well beyond anything we offered in Nea! This is :sparkles: something entirely new :sparkles: for email editing at Mailchimp. And we’re already hearing it called a game changer. Amazing work, team!!
Reactions: 100_rainbow (22), raised_hands (5), lets_go (6), raised_hands::skin-tone-5 (1), raised_hands::skin-tone-2 (2), raised_hands::skin-tone-4 (1), raised_hands::skin-tone-3 (1)



---

=== Message from Emily May Curtin (U02K6JTUE4X) at 2026-04-13 12:35:32 PDT === 
Message TS: 1776108932.397139
*Launched and Landed | MC Business App Enablement* :rocket:

:sad-cat: *The Problem*
You’re a builder. You’ve got Claude, you’ve got ideas, and you’ve built an app on your laptop. It’s really great, it’s super useful, you’ve shown your team and they love it. The problem? You “just” need a place to deploy it; a place that’s secure, governed, compliant, monitored...

:boom: *Solution*
Introducing MC Business Enablement Apps: your idea + our structure = velocity for the business!

:rocket: *What Launched:*
MC Business App Enablement (mc-bi-rapidexp) is a purpose-built prod environment and monorepo for internal apps built on Mailchimp’s BigQuery data. It includes:
• A shared GitHub monorepo organized by team — clone it, let Claude scaffold your project, open a PR, and your app is deployed automatically on merge.
• AppEngine Flex hosting behind IAP — apps are secure and internal-only by design,• Templates for AppEngine apps, MCP servers, and docs sites.
• An AI-first developer experience — CLAUDE.md files guide Claude through repo conventions, config, and deployment so you can go from idea to PR without engineering help.

:mag: *Who It’s For:*
Any non-engineer at Mailchimp who has — or wants to build — an internal app on top of BigQuery prod data. Sales Ops, Data Science, Finance, Analytics, and beyond. If your team produces data and you want a tool that uses it, this is for you.

:lock: *Guardrails Worth Knowing:*
• BigQuery/GCP only (reach out for cross-cloud needs)
• Prod data only (`mc-business-intelligence`) — get your data into prod first, then build on it.
• Internal use only. This is not for anything C1-facing.
• Engineering reserves the right to intervene (with notice) for reasons of compliance, security, etc.

:footprints: *What’s Next:*
• Exploring AWS deployment for IDL data
• Researching possibilities of 3rd party APIs

:tada: *How to Get Started:*
1. Join *<#C0APX9W8YU8|mc-business-enablement>* and say hi!
2. Request BigQuery prod read access if you don’t have it (one-time)
3. Take the developer training quiz (one-time — required before we grant access)
4. Clone the repo, let Claude create your project in your team folder
5. Test locally, Claude tells you how to test locally to make sure everything is working 
6. Open a PR — app ships on merge to the main branch.
Docs: <https://devportal.intuit.com/app/dp/capability/CAP-2726/capabilityDocs/main/docs/usecases/build-a-business-app.md>

:data_party: *Huge thank you to the team:*
Engineering: <@U02K6JTUE4X|Emily May Curtin>, <@U054QT37B1C|Chaitanya Pantar (CP)>, MC Data Engineering
Early Adopters/Champions:
• Sales Ops: <@U07SF0TTRM5|Paul Kundel>, <@U07EFT25CBB|Stuart Chuang>, and the _whole_ Sales Ops team! 
• Finance Analytics: <@U05FNQPLGCW|Ben Ou>, <@U06TM5M3REY|Walker Turbyfill> 
:rocket: And what would this announcement be without examples! Just a few, and just the beginning!
• <https://wbr-copilot-dot-mc-bi-rapidexp.ue.r.appspot.com/|WBR Dashboard> by <@U07SF0TTRM5|Paul Kundel> 
• <https://sp-mece-nonmece-dot-mc-bi-rapidexp.ue.r.appspot.com/|SP MECE/Non-MECE Dashboard> by <@W0187J1KT51|Tyler Frazer> 
• <https://mm-acquisition-dashboard-dot-mc-bi-rapidexp.ue.r.appspot.com/|MM Acquisition> by <@U06F5BHKT1T|Christina Cook> 
Reactions: data_party (4), nice-neon (5), nice-pink (5), heart (4), awesome (4), congratulation (4), blue_heart (2)



---

=== Message from Kristen McDonald (W8GN50J8P) at 2026-04-13 13:15:05 PDT === 
Message TS: 1776111305.116139
:tada: *GoDaddy QB Free and Mailchimp Pilot Test is now LIVE (4/10)!*:tada::qbo::mailchimpie::godaddy:

• *What* :rocket_launching:*:* Six-week "light pilot" on three high-intent GoDaddy surfaces to validate QuickBooks Free and Mailchimp as a scalable acquisition engine for solopreneurs, aiming to secure a long-term distribution partnership over Xero and Klaviyo. 
• *How* :testing:*:* The QBO Free pilot will be overseen by GPE’s Platform Partner, Partner Marketing, and product marketing team and require only minimal resources and use the existing <https://quickbooks.intuit.com/oa/online/free|QBO Free marketing page>, copy, and CID infrastructure and Mailchimp’s <https://mailchimp.com/pricing/marketing|14-day trial landing page> . GoDaddy will place both Free ads on high-visibility GoDaddy surfaces. All of these ads will redirect (with custom CID or UTM) to. More details<https://docs.google.com/document/d/1VxY8fnxdlAeI6rgz6cWAWlFdiDv9XpgI32xU4OqWSNQ/edit?tab=t.9662puy5oygz| here>.
• *Timing* :calender:*:* Launched on 4/10 and will run for an estimated 6 weeks. We expect to generate 20K to 40K impressions.
• *Metrics* :metrics-team:*:* Based on GoDaddy’s experience in the other  pilot’s, we will monitor three metrics:
    ◦ Click-through-rate (CTR; reported by GoDaddy)
    ◦ Sign-up rate greater (reported by Intuit)
    ◦ 30-day free-to-paid conversion rate greater than 10%
• *Why this matters* :twinparrot:*:* Successfully testing this partnership with GoDaddy creates a strategic acquisition channel to reach early-stage SMBs during critical business formation moments. A positive outcome establishes the foundation for a long-term resale relationship across QuickBooks and Mailchimp, directly accelerating towards our FY27 goals for 1M QuickBooks Free sign-ups and new Mailchimp bookings growth.
*TREMENDOUS THANK YOUS to all who helped push this across the finish line so quickly*  :hugging_face:  
*Can't wait to see what we learn and grow together!!*

• *Partner Marketing:*<https://intuit.enterprise.slack.com/team/W8GN50J8P| @kmcdonald1>,<https://intuit.enterprise.slack.com/team/U079XLXJ338| @Allie Strack >
• *PMM:*<https://intuit.enterprise.slack.com/team/WP9UB5SN6| @dklein3><https://intuit.enterprise.slack.com/team/W8FL7070S| @ctorres4>
• *Product:*<https://intuit.enterprise.slack.com/team/U0918C5D71V| @Adi Srinivasan> <@U08ETVD4YTV|Alex O'Reilly> 
• *Platform Partners:* @<https://insight.intuit.com/profile/gstarr|Garrett Starr>
• *Data Science:*<https://intuit.enterprise.slack.com/team/U090U4DK170| @Fuqin Yan>
• *MC Analytics:* @/wes <@U08AJ93H7R6|Russell Cheng><https://intuit.enterprise.slack.com/team/U03A7587ZSB| @Samuel Zhu>
• *Platform Partners PgM:* @<https://insight.intuit.com/profile/rmoore19|Richard Moore> @<https://insight.intuit.com/profile/akhanka|Abhinav Khanka>
• *Intuition MC:* <@U09MHG0MH36|Lisa Rae Bowman> <@U0A1PLR7BU7|Constantina Kokenes> <@U09QF7NMYR2|Lisa Qin> <@U0AJVH9PTRD|Paul Twa>

Reactions: yes3 (1), raised_hands (1), nice-pink (1)
Files: QuickBooks Image_GoDaddy.png (ID: F0ASHM7J96H, image/png, 206.0 KB), Mailchimp Image_GoDaddy.png (ID: F0ASHM89E4V, image/png, 103.9 KB), GoDaddy Testing Brief (ID: F0ALRC5RPV1, application/vnd.google-apps.document, 0 Bytes)



---

=== Message from Payton Camilli (W012EU6L7FG) at 2026-04-14 15:22:56 PDT === 
Message TS: 1776205376.985479
:mag_right: :rocket: *x290 Experiment Launched: Inline Contact Search in Audience*  :rocket::mag_right: 

We've officially ramped `aorg.inline_contact_search` to 100%! Full experiment details below.

:test_tube: *Problem & Hypothesis:*
If we introduce an inline contact search experience that lets users search on more of their data, search usage will go up and sort usage will go down. Because sort → action workflows take a full minute longer than search → action workflows (3 min vs. 2 min), this will save users time and ultimately drive higher campaign creation.

:question2: *What changed?* From :pensive: → To :heart_eyes:
• Inconsistent with global search → _Consistent results (same CDP API)_
• Search on first name, last name, email, phone only → _Search on ALL visible custom merge fields (string, date, and more)_
• Takes you out of context to a new page → _Stays inline, results appear directly in the contact table_
• Must click enter to get results → _Results appear as you type_
• Limited data in results → _Full contact table data visible for easy comparison_

:boom: *Why we think this will work:*
• _66.3%_ of users who use table search go on to create a campaign within 7 days vs. _58.3%_ who don't use search at all
• Users who complained loudest when search disappeared were relying on sort as a fallback — a better search removes the need for that workaround entirely

:chart_with_upwards_trend: *What we're watching:*
_Primary Metric_ = Campaign Creation Rate within 7 days of table search (baseline: _62%_)
_Secondary:_ Table Search Usage Rate (baseline: 19.4%), Sort Action Rate (baseline: 10.5% — we expect this to decrease)

:books: *Resources*   •  <https://docs.google.com/document/d/1rRvr6olmHxOj8bt6QhnB9M8XMjN-3ehuc0rq3XgwDcQ/edit?tab=t.0|EDD>  •  <https://docs.google.com/document/d/1jc1w77CYBMs-AiIimGJDtA8ZbKcum7daFjQZ_Eug0ik/edit?tab=t.0|PRD>  •  <https://app.amplitude.com/analytics/intuit-portfolio/dashboard/6alju9m4|Amplitude Dash>  •  <https://jira.cloud.intuit.com/browse/AORG-7847|Jira Epic>  •  <https://wiki.cloud.intuit.com/wiki/spaces/ACS/pages/3622535552/26.04.08+-+Sprint+44+CDP+Inline+Search+Experiment|Release Plan>

:next: *What's next?*
• Watch for <https://de.dash.a.intuit.com/ema/?tab=exp_detail&exp_id=9300003094894&subtab=sub-summary|results> over the next ~3 weeks (Bayesian model will call it once there's enough signal)
• Questions? Drop them in <#C08GFCSCPHT|mc-aorg-prj-cdp-all-contacts>

:mega: *Who made this possible?* :mega:
• _Audience:_ <@U05G24X48C9|Mario Merendino> <@U02KMC4S798|Khadijah Parks> <@U063VQYDNQ5|Livia Gimenes> <@U03FZ581XTR|George Nakkas>  <@U07USKD0MA5|Shefali Dalal> <@U08CE9D9QKS|Patrick Kopps> <@W012EU6L7FG|Payton Camilli>
• _CDP:_ <@WA3PKCN66|Jessica Lin> <@W8FL3HEMQ|Navjot Cheema> <@U078B7PT3A8|Dan Damkoehler> <@U04SC218QQ3|Sijia Liu> <@U0789R246JY|Leila Jalali> <@U09SXRRBJ73|Ryan OConnell>— incredible partners on this one, CDP indexing data for search was the key dependency that unlocked the whole experience :heart:
Thread: 7 replies (latest: 2026-04-27 14:26:43 PDT)
Reactions: awesome-star (12), cdp2 (7), rocket (11), yes3 (2), raised_hands (1), clapping-all (2)



---

=== Message from Marissa Rivera (U02LB3HSDRN) at 2026-04-17 12:46:33 PDT === 
Message TS: 1776455193.630409
:rocket: *Nuni Inline Image Editing and Cropping*

Resurfacing this release announcement to share some great VoC with the tagged team members responsible for this release! An agency partner at BigCookie has been supporting THE Elton John with their marketing efforts. They just sent in unsolicited feedback about this feature. Their exact words: *"OK, Mailchimp has literally made my day. Cropping images IN THE EMAIL. incredible."*

Huge props to the whole team on this one. Well done! :raised_hands: :eltonjohn:
Reactions: clapping-all (14), freddance (5), eltonjohn (4), nice-neon (1)
Files: product feedback_elton john.png (ID: F0AUJN8D40G, image/png, 100.7 KB)



---

=== Message from Connor Callahan (U02KPE15PCL) at 2026-04-20 12:05:08 PDT === 
Message TS: 1776711908.028079
:satellite: *Launched | <https://github.intuit.com/pages/ccallahan/registration-watchtower/|The Watchtower>*  :sms1: :tower: 

Here with a slightly different launched post than usual in hopes that teams get value out of the Claude co-work+github+pages pattern within.

:notess: *Context*
• We operate SMS in 37 countries. Changes in regulations and registration are inevitable. Until now, our best-case for change notification was 2–4 weeks, and our worst case was finding out _after_ the change was already live, as happened in Ireland recently.
• Friday, once again we found out late about an emerging change in Finland with 2 weeks to the deadline. 
• Saw a better way with AI so built one: _<https://github.intuit.com/pages/ccallahan/registration-watchtower/|The Watchtower>_ is an AI-powered proactive intelligence system that monitors every live market, every week, without waiting for anyone to tell us.
    ◦ :book: <https://github.intuit.com/pages/ccallahan/registration-watchtower/|Live dashboard>
    ◦ :github: <https://github.intuit.com/ccallahan/registration-watchtower|Repo>
    ◦ Built in 3.5 hours from need to value.
:white_check_mark: How it works
• _Scans all 37 live country markets every Monday morning._ Looks at regulators, key legislation, and industry signals, tuned by sender type
• _Flags only net-new risks, rumors, or confirmed facts:_ no re-alerting on known issues.
• _Posts directly to the messaging leads channel_ when something new is detected, so the team can triage proactively.
• _Maintains a living library_ on our GitHub page, a running record of every flagged change, by country. 
:boom: *Paid for itself the first time it ran*
• Built Friday, and this Monday we detected an upcoming registration change in *Spain _50 days before it takes effect._ Giving us literally double (2X) our time to develop a solution* 
• That's the difference between a roadmap interruption and a calm, well-sequenced response with more time to build something customers actually love.
:gear: *How it's built*
• Scheduled Claude Desktop Coworker task + GitHub repo + GitHub Pages. The task runs on a schedule with push and Pages admin access to commit research and keep the library current. If your team monitors a domain where you need proactive detection and you're still waiting for someone to tell you, this pattern is fork-able.
:next: *What's next*
• Currently working on a quick start guide for using co-work+GH+Pages so that you can one shot setting up the basic frame with your own teams.
• A *Proactive Messaging Competitive Market & Sentiment System*
    ◦ :check-5853: *Claude Co-work scheduled task doing always on research on competitors, social channels, and more.*
    ◦ :check-5853: *GH Repo as store of truth*
    ◦ :check-5853: *Public page with aggregated insights ( always updated )*
    ◦ :check-5853: *Slack notifications* 
        ▪︎ Daily/Weekly flag (Negative customer feedback on reddit, and other social signals) 
        ▪︎ Weekly digest of (New core messaging features from competitors)
Thread: 4 replies (latest: 2026-04-22 05:51:21 PDT)
Reactions: booms (7), nice-pink (15), clapping-all (2), flag-fi (1), ireland (1)
Files: The Watchtower.mov (ID: F0AU7Q8DL5A, video/quicktime, 279.7 MB), Post.png (ID: F0AU472JALS, image/png, 334.4 KB)



---

=== Message from Srilekha Chandrashekar (U02KEQBFEJ2) at 2026-04-21 06:00:08 PDT === 
Message TS: 1776776408.288969
:rocket_launching: *Product Launch: <https://mailchimp.com/integrations/meta-custom-audiences/|Meta Custom Audience Integration >: General Availability*

We are excited to announce the launch of a direct, real-time sync between *Mailchimp and Meta Custom Audiences*. This integration removes the friction of manual CSV uploads, allowing users to automate their targeting and retargeting efforts across Facebook and Instagram.
*The Value Proposition*
• *What was launched:* A seamless sync that connects Mailchimp segments directly to Meta’s Custom Audience platform.
• *Why it matters:* It eliminates manual data exports, ensuring social ad audiences are always synced with the latest CRM data.
• *Why users love it:* It unlocks high-precision retargeting (like cart abandoners) and powers high-quality Lookalike audiences to find new customers more efficiently.
*The "Full-Cycle" Lead Strategy*
This integration creates a powerful feedback loop: users can capture high-quality leads via *Meta Lead Ads*, sync them to Mailchimp, and immediately push them back into Meta Custom Audiences to refine targeting. Our experiment results already show a *meaningful lift* in users connecting their Lead Ads to this integration, proving the demand for this full-cycle automation.

*Early Adoption & Results*
One of our premier clients, *C3*, has already begun leveraging the integration, and we look forward to sharing their performance feedback soon.

:pray: *Team Kudos*
This was a massive cross-functional effort. A huge thank you to everyone involved in bringing this to life!
Engg : <@U02KJFNSB6H|Philip Allen> <@U085B0VAFHV|Nalin Ahuja> <@U07A05V0H5J|Stephen Komae> <@U031T5Y29HC|Rohit Mereddy> <@U02UW4TGH53|Samatha Gajula> <@U049D5NR1HC|Aravind Rajendran> <@U078M0WH6RH|Nirmalamary Charles> <@U01HJ6ZRH44|Francois Beaussier> <@U046BHCFXEE|Nilesh Nayak> <@U02KJ6V3LA1|Cody Solomon> <@U0517L5N34Y|Avery Felman> <@U065HQK3ZBQ|Somya Agarwal> <@U03FR4962NR|Russell Sidney> <@W8FJ04FH9|Andrei Khmelnitski>
Design : <@U07KKEVS695|Skye Hurley> <@U05DQHZTQ3T|Jane Krause> <@U0AHB56P8RW|Lauren Shupp> <@U02KPGZ4HHS|Jane Guthrie>
TPM : <@U07PJK7TTPE|Brooke Addison> <@U03R9TTF7FY|Abby Barnett> <@U06B46M7E5N|Sunita Yadav> <@U07USKD0MA5|Shefali Dalal>
Product & Partnerships : <@U07DWUY7AKA|Josh Wilkinson> <@W8FMBKWMS|Siddhartha Misra> <@U03KUBTCSG1|Frank Persico>

Thank you all for your hard work and dedication! :yellow_heart:

Here is the <https://www.loom.com/share/60ba1ccfd76e46eeac5b343f41ba5661|demo> of the Meta custom audience integration

*What's next*
• *Enhanced Sync Diagnostics:* We are developing post-setup visibility tools to give users real-time feedback and confidence in their data sync health.
• *1-Click "Send to Meta":* We will soon introduce a direct shortcut on the segmentation page, allowing users to push audiences to Meta with a single click.

Thread: 3 replies (latest: 2026-04-27 06:25:58 PDT)
Reactions: claps (6), celebrate (9)



---

=== Message from Nitish Pandey (U02KMFB0Z19) at 2026-04-21 11:05:43 PDT === 
Message TS: 1776794743.175059
:rocket: *LAUNCHED: MC Internal Data Agent*  :data-wolf: 

:mag_right: *Customer Problem*
MC customer data is powerful, but accessing it has never been easy. Data is spread across multiple tables and data stores, and making sense of it typically requires domain knowledge or an analyst skill set. For most of us, that's meant a significant barrier to getting quick, informed answers about our C1 customers.

:boom: *What Launched*
The *MC Internal Data Agent* lets you ask questions about Mailchimp C1 data in plain English and get answers instantly, no SQL required. It gives Leadership, PMs, and anyone who needs fast customer insights direct, governed access to MC data through natural language. It includes:
• *Unified Data Access:* query across 5 MC datasets (348 tables) [bi_reporting, bi_activities, bi_lookup, mailchimp, bi_inferences] for insights, table discovery and more.
• *Natural Language Querying (NLQ):* ask in plain English; the agent handles the rest
• *Customer Voice:* surface pain points, hidden concerns, and feature sentiment from user research interviews
• *Nuni Editor Feedback:* uncover usage patterns and insights from tens of thousands of Nuni email editor prompts
• *Semantic Layer:* A shared understanding of our data built into the agent's reasoning, so when you ask about "churn" or "active users" it knows what you mean and where to find it.
:door:*How to Access It*
• _UI:_ <https://mc-data-agent-ui.app.intuit.com/mc-int-data-agent-plugin/mcintdataagentuiplugin|Internal Data Agent> (log in with Intuit SSO)
• _Slack:_ Tag <@U0ALP88R14P|Ask Internal Data Agent> in <#C03TKTSPDCK|business-intelligence> and start a thread. Respond :+1: or :-1: to rate answers
• 2-minute <https://drive.google.com/file/d/10agkvaE6VRs0Z3eRxSUdkImD4LqejKMT/view?usp=sharing|video> of what the UI experience looks like.
:warning:*A Note on Accuracy*
This is an LLM-based solution. We've built guardrails but the agent can make mistakes. For high-stakes decisions, please validate with an Analyst or Data Scientist.

:black_right_pointing_double_triangle_with_vertical_bar: *What's Next*
We're just getting started! We're actively looking for feedback and real-world use cases to help us iterate, including ones we haven't thought of yet. Planned next phases include:
• Integration with Image Generation Tool
• Role Based Access Control
• Addition of more datasets
Have feedback or feature request? Reach out in _<#C0A6VC5AEMD|mc-internal-data-agent>_ or via this Google <https://docs.google.com/forms/d/e/1FAIpQLSc9oVVcahZitg3-unteh8BdCtipVl2mRJ4_PikJo874ZcuZyg/viewform|form>.

:mega: *Huge thank you to the team:*
Data Engineering: <@U02KMFB0Z19|Nitish Pandey>, <@U043P7Q7EJW|Mei Zhou>, <@U0740T88AU9|Neha Tarey>, <@U0726KANNG6|Baris Dundar>  <@U02KP74TMT6|Brian Holbrook> <@U02K6QR60P9|Roman Rheingans-Carrion> <@U02KMCPUWEP|Emmett Bamford>
DS: <@U02R5B0HN4F|Vlad Khvan>
TPM: <@U02KMG9SNP4|Simone Shahdadi>
PD Leadership: <@U02K6NWDM7H|Marlene Mayfield>, <@W8Z0471LH|Rushit Patel>
Reactions: boom (20), data_party (24), rocket-party (13), tada (14), rocket (12), yay (7), clapping-all (14), eyes (5)



---

=== Message from Jacquelyn Horgan (U02KMAN6V1R) at 2026-04-22 06:03:14 PDT === 
Message TS: 1776862994.666289
:tada: *Launched: Place of Supply–Based Taxation* :globe_with_meridians::white_check_mark:
_Rollout began April 17 and reached 100%  on April 21_

:mag: *Background*
Intuit has a responsibility to collect and remit accurate taxes in every country where we operate. International Indirect Tax laws require that a customer's location be determined using _two or more non-contradictory data points_. Until now, Mailchimp was using only a single data point — the primary contact address — leaving us at risk across all international markets.

:bar_chart: *What Changed*
Mailchimp now determines a customer's tax location by evaluating multiple data points and asserting a country when at least two match. We now use the _Assessment Country_ as the source of truth for tax.

:dart: *Why It Matters*
_Compliance risk:_ Without two matching data points, we lose the "legal presumption" of location. In an audit, the burden of proof shifts to Intuit to justify every single transaction. Repeated failure in certain regions can result in countries blocking Intuit from operating there entirely.
_Financial risk:_ If a tax authority challenged our methodology and assessed for under-collected VAT, Intuit is liable for the principal tax in that country. Most countries also assess penalties of _30–100% of the unpaid tax amount_, plus backdated statutory interest. We operate in 70+ countries, each with different rates and penalty structures.

:hammer_and_wrench: *What the Team Had to Build to Make This Possible*
This wasn't just a configuration change — the team had to close significant data gaps from scratch:
• :phone: _No phone country data existed_ → Built and shipped a brand new Phone Number Component with standardized international dialing codes, now collected at sign-up and checkout
• :computer: _Only last login IP was stored_ → Began actively collecting and retaining Owner IP address for location assessment
• :credit_card: _Payment method country wasn't available_ → Worked across _3 payment processors_ (Adyen, PayPal, Chase) to collect funding source bank country and state
• :card_index: _No assessment infrastructure existed_ → Created and back-filled an Assessments table for _over 1 million users_
:chart_with_upwards_trend: *Impact by the Numbers*
While Place of Supply evaluates tax location for ~1M+ paid accounts across 70+ countries, the team's precision meant real-world disruption was minimal:
• _98.7%_ of customers validated to primary contact country
• Only _0.5%_ of our annual paid base will see any change to their tax rate
• Of those impacted, the change is _net neutral_ — customers moving to a higher tax rate are offset equally by those moving to a lower one

This is the result of nearly two years of careful data collection, assessment logic, and cross-functional execution — ensuring we could meet a critical compliance requirement without disrupting the overwhelming majority of our customers.

:rocket: *Key Capabilities Shipped*
• Evaluates 2+ non-contradictory data points to assert tax location prior to every transaction
• Assessment evidence stored at the transaction level for 10 years to meet data compliance requirements
• Dynamically re-assesses every 4 months or when key data points change 
• UAE Emirate and Canada Province fields added for correct sub-national tax treatment
• Assessed tax country, state, and assessment reference number now written to orders
:people_holding_hands: _Thank you to the incredible cross-functional team that made this possible — this has been a long time coming and is one of the most important compliance initiatives Mailchimp has shipped!_ :raised_hands:

• *PD:* 
    ◦ FINOPS:<@U044UN28H6C|Sreeram Jayan> <@U045KSM7L8L|Mathew Deeb> <@U06RXPP6HNU|Nikhil Kassetty> <@U04623EPG8H|Hunter Ray> <@U0670DW10HY|Vrushali Ghodekar> <@U02KMFA7R2N|Ryan Simpson> <@U07QFCDAV6X|Aravindhan Kumar> <@U06GM26KU3U|Keerthi Joseph> <@U07SM68NTBL|Jonathan Robinson> <@U043L8T756Z|Knut-Sigurd Knuteson> <@U047HMUGE82|Erin Szarpa> <@W01BKFS7N8P|Navreet Kaur>
    ◦ MSE: <@W8FQBF06R|Moolemane CB> <@W9NUCFL65|Hafeez Rasheed> 
    ◦ MC Data Team : <@U0886F7RZBJ|Krunal Shah> <@U02KM8333RQ|Brad Mayfield> 
    ◦ XP: <@U07EHFAQJDD|Taylor Martin> 
• *PM:* <@U02KMAN6V1R|Jacquelyn Horgan>
• *XD:* <@U02KM9USVDY|Greg Clark> <@U02LB7537J4|Zac Wall> 
• *Legal:* <@W8FL7249G|Katherine McLain (she/her)> <@U0526027H5F|André M. Board> <@U02L00GFMEV|Koleen Henson> <@W01AY0ECQ59|Paula Brunoro> 
• *Finance* : 
    ◦ FARM: <@U02KJDWAHCM|Matt Fiedler> <@U032GEW7U0Y|Brent Hallinger>
    ◦ Payments: <@W8FL4GW4A|John Mattison> <@W8FQAGQLV|Patrick Fenoughty> 
    ◦ International Indirect Tax: <@U03DB0STD1P|Zia Uddin> 
    ◦ US Indirect Tax: <@W8FMC5VD2|Dean Henderson> <@W8FJ03X3M|Pete Hernandez> 
    ◦ FDTG: <@U02TNUQ1868|Srinivas Manepalli> <@U07T62F35V3|Geetanjali Goyal> 
• *TPM:* <@U07USKD0MA5|Shefali Dalal> <@U06R90N9A6N|Suzanne Kirkpatrick> <@U07PV9VL1HD|Omar Carrasco> 
• *Comms & Technical Content:* <@U02KEHPFLDU|Elizabeth Cason> <@U02K6K3VC2K|Emily Roberson> 
• *Care:* <@U02KJD0UBBP|Laura Thompson> <@U02L049UBQ9|Stephen Gray> <@U02KMGYSHK4|Victoria Velarde> 
• *Leadership:* <@U07MYEG53JB|Rhomaro Tesfai-Powell> <@U02V0Q6K27P|Yilmaz Kara> <@W8S0AML9M|Gavin Buckley>
Thread: 4 replies (latest: 2026-04-22 08:41:35 PDT)
Reactions: celebrate (12), clapping-1772 (8), yay (7), yes3 (4), praisethesun (1)



---

=== Message from Lovey Saini (U09T98KLGHK) at 2026-04-22 09:50:13 PDT === 
Message TS: 1776876613.408419
:rocket: *Mailchimp x ChatGPT & Claude — Our Largest Release Yet is Live!*

:rocket: Big week for MC in 3P AI surfaces. Here's what shipped and why:

:sparkles: *New Features:*
• *Campaign plan reasoning:* The rationale behind recommendations is now surfaced directly in the UX
• *Content generation templates:* Templates are now matched to inferred customer profile for more relevant starting points (e-commerce & pro services)
• *Image editing:* Users can now edit images inline with a prompt
• *Personalized Benchmarks:* Every account now receives personalized, data-driven benchmarks powered by weighted averaging across 30+ new context signals and 25+ peer benchmarks at P50/P75/P90. Instead of generic advice, users now get specific insights like "Your open rate of 36% is at P75 for businesses like yours; your bounce rate of 2.1% is above median, suggesting deliverability work before scaling."
:earth_africa: *Expanded Availability*
We're now live in Canada, Australia, and the UK — reaching ~20% more of our active customer base.

:pray::skin-tone-4:*Huge props to the whole team for getting this across the line and many peers along the way*. Please feel free to reach out to any one of us for any questions or thoughts. CC: <@U09QF7F45AQ|Nathan Snell> <@U08ALKME0VA|Inder>
• TPM: <@U0725TR032M|Katherine Powell> 
• BD Partnerships: <@W8FMA0G2G|Shruti Hegde> 
• Eng: <@WRHEEP39A|Mehrshad Sahebsara> <@W8FM8TSDS|Gunjan Raghav> <@U0A8H8JL4JV|Pranav Deshpande> <@U07GLH2MT32|Alex Malokin> <@U05B8V54DC0|Rich Archer> 
• Design: <@U03MENW19HA|Isabella Scheier> 
• QA: <@U02LB056SQ0|Essence Coleman>
• Data Science: <@U03BZL23C1F|Heuisu Kim> <@U091QJQCRMZ|Yiwen Yan>
:demo-2:Here's a <https://drive.google.com/file/d/1N9MMOPmPukncdwfYjCMzLwtDok8QxWzi/view?resourcekey|demo> of the current experience on Claude
Reactions: claude-code-intensifies (17), rocket_launching (13), rocker (4), party-blob (5), clapclap (2), pet-claude (3), freddance (1)
Files: Claude-V1.mov (ID: F0AU9GTL5NJ, video/quicktime, 68.5 KB)



---

=== Message from Jacquelyn Horgan (U02KMAN6V1R) at 2026-04-23 08:31:34 PDT === 
Message TS: 1776958294.420039
Hello, everyone! PLC and Dotcom are excited to announce that our *Annual Plan Self-Serve experiment* is officially live. :fredwave:

:blob-why: _*Why Annual Plans?*_
Two FY26 input goals — and we need wins on both:
• _Scaled Acquisition via <http://Mailchimp.com|Mailchimp.com>_: $3.1M FY26 target
• _Scaled Churn Reduction:_ $14.9M FY26 target

Annual Plans attacks both by lowering our opening price point, moving Standard and Essentials to trial-only start, and simplifying our dotcom merchandising strategy — with a clear incentive that aligns us with competitors and locks in a longer term commitment.

:sparkles: _*What we launched*_
Monthly vs. annual billing toggle for _prospective customers_ on <http://Mailchimp.com/pricing|Mailchimp.com/pricing> and trial flows, and _existing Free customers_ on plan selector and checkout. Run time is 4 weeks.
• _Control (34%)_: Current experience — free trial or 15% off
• _Variant (33%+33%)_: Annual at 20% off, one defaulting to monthly, one to annual

Standard and Essentials: 14-day free trial, then monthly or annual. Premium: monthly at list price or annual at 20% off.

:tada: _*Two Mailchimp firsts*_
• :one: First-ever _rate card experiment_ — a dedicated annual rate card at 20% off, separate from monthly list price
• :two: First-ever _billing term experiment_ — prospective customers choosing monthly vs. annual at purchase

We may not nail it on the first pass — and that's okay. The learnings will be critical to getting us where we need to go.

:chart_with_upwards_trend: _*What we're watching*_
• AP Take Rate: >10% of new bookings on annual
• Prospect to Booking Rate: +2.5% lift (baseline ~25K/month)
• 90-Day Retention: +3pts (baseline 67%)
• NB MRR: $70K in-year FY26 / $1.3M–$3.9M incremental FY27

:mega: _*Thank you to the incredible cross-functional team!*_
PM: <@U02KMAN6V1R|Jacquelyn Horgan> <@U02LARVGVGQ|Amanda Hunt> <@U07MYEG53JB|Rhomaro Tesfai-Powell>
PD:
• FINOPS: <@U07SM68NTBL|Jonathan Robinson> <@U0A08A23ZK9|Prithviraj Sengupta> <@U06GM26KU3U|Keerthi Joseph> <@U02KMFA7R2N|Ryan Simpson> <@U04623EPG8H|Hunter Ray> <@U045KSM7L8L|Mathew Deeb> 
• Plans: <@U045QK7AM1A|Anesia Smith> <@U02KEAE3DL6|Bryce Hammond> <@U05NALW1S3U|Collins Amadi> <@U04F7GC809E|Poornima Padubandla> <@U07U1BMMJ3V|Sandeep Kumar> <@U029B9R59JQ|Divya Ramchandani> 
• DOTCOM: <@U03TAMS8ATF|Tommy Yates> <@U032WKWKF2P|Harshada Desai> <@U02K6F0T9LP|Anna Sheaffer> <@U02KM08JQR0|Aaron Armstrong> <@U033B9J9GQL|Nicole Newton> <@U033P0AEQ5A|Zach Hall> <@U03ETSQ5A1K|Jeremy Tillman> 
PD EM: <@W01BKFS7N8P|Navreet Kaur> <@U02URC9KK46|Lawrence Ma> <@U047HMUGE82|Erin Szarpa>
Design: <@U09B92CRAM7|Sebastian Caceres>
DS: <@U031MMBFLBC|Ethan Ham>
Finance: <@U02TNUQ1868|Srinivas Manepalli> <@U05QNVD0KHP|Cuc Le>
Legal: <@U02L00GFMEV|Koleen Henson>
Leadership: <@U0A8293TH9U|Anish Nahar> <@U0A99U871KR|Sid Bakhru> <@WERJCJ189|Kyle Spaulding> <@W8XEU93GS|Cesar Rodriguez>
Thread: 17 replies (latest: 2026-04-28 13:20:41 PDT)
Reactions: celebrate (22), yay-frog (9), clapping-all (10), moneyfred (3), dance_vibe (1), raised_hands (1)
Files: Annual Plans_ E2E Experiment.pdf (ID: F0AUS29EQQM, application/pdf, 628.7 KB)



---

=== Message from Crystal Ju (U08AHM96D2L) at 2026-04-23 16:11:02 PDT === 
Message TS: 1776985862.975519
Hi all, Since you are customers of IPS, we are excited to share two milestones from the IPS (Intuit Persistence Services) team:

:dart: *TY25* *Tax Season*
• *328B* total transactions served (*143% YoY*), *3PB* of data was stored with *464TB* during peak, with *100*% availability during peak and 99.999% availability for the entire season. Directly contributing *$225M+ in* revenue-generating product experiences:
    ◦ *IPS NoSQL:* CDC 2.0 with *$18M revenue* and Checkmate (TRDR) with *$35M revenue.* Peak Throughput: 359K TPS (150% YoY // 240K in TY24; tested up to 779K TPS).
    ◦ *IPS Relational:* 2x TY24 volume, enabling Expert appointments, routing, and crypto in TTO. Total Data stored: 34.1 TB (~6700% YoY // 510 GB in TY24). peaked at 3,500 TPS, serving 5.6 billion transactions for the full season (170 million during peak).
    ◦ *IPS OLAP:* *$15M revenue* (700% YoY from $2.2M), 12x query throughput on 3.5x less compute. Peak Query Throughput: 712 QPS (1200% YoY // 60 QPS in TY24). Peak Ingestion Throughput: 75.5K TPS.
    ◦ *IPS Cache:* Powered UCM + FDR with *$158M combined revenue.* peaked at 29K TPS, total 4.5 billion queries and wrote 32 TB of data across the season, maintained a TP99 query latency of 9 ms. 
    ◦ *IPS Search/Vector:* peaked at 10,173 TPS and 1.1 billion searches, and served 11.7 billion total for the season. This was the first season Sales Catalog (Finish & File, TTO) was powered by IPS Search, and Semantic layer for Chat4U and HelpGPT, Intuit's GenAI powered by IPS Vector.
:rocket: *IPS Plugin V1 Launch*  :rocket:
In parallel, the IPS team launched a full capability plugin in the Intuit DevAssist Platform, bringing persistence as an AI-native capability into the developer's IDE.

*How it works:* A developer describes what they need in natural language (e.g. "I need to store user tax documents"), and the IPS plugin handles database selection, compliant schema design, PR generation, QA deployment, and SDK code generation end to end.

*Early results:* A CG alpha team tried migrating from RDS to IPS Managed Relational, compressed a multi-day workflow to approximately 1 hour using the plugin.

*What's covered:* All 8 IPS datastore products via 9 purpose-built AI skills (NoSQL, Relational, OLAP, Cache, Search, Vector, Graph, Database-Selector, and IPS-Self-Service Provisioning), with built-in compliance (PII/7216 tagging) and Intuit IAM authentication.

*Getting Started:*
*Installation*: npx @dev-platformexps/devassist-plugin-manager@latest add ips-plugin
*Documentation:* Our team is piloting a "Compass, not Encyclopedia" principle — prioritizing actionable navigation over exhaustive docs:
• <https://devportal.intuit.com/app/dp/capability/aak8rk1uemiq3v32ktct/capabilityDocs/main/docs/getting-started.md|Get Started with IPS NoSQL>
• <https://devportal.intuit.com/app/dp/capability/CAP-2775/capabilityDocs/main/docs/getting-started/getting-started.md|Get Started with IPS Relational>
• <https://devportal.intuit.com/app/dp/capability/CAP-2775/capabilityDocs/main/docs/getting-started/getting-started.md|Get Started with IPS OLAP> 
• <https://devportal.intuit.com/app/dp/capability/CAP-2778/capabilityDocs/main/docs/getting-started.md|Get Started with IPS Cache>
• <https://devportal.intuit.com/app/dp/capability/mm666693z0vrzid5hrdn/capabilityDocs/main/docs/ips-search-let-me-try.md|Get Started with IPS Search>
• <https://devportal.intuit.com/app/dp/capability/CAP-2074/capabilityDocs/main/docs/onboarding/let-me-try.md|Get Started with IPS Vector>
• <https://devportal.intuit.com/app/dp/capability/u982o0t1bnbcfmwej9cz/capabilityDocs/main/docs/getting-started.md#three-simple-steps|Get Started with IPS Graph>
*What's next:* We're incorporating alpha team feedback, improving discovery and onboarding, and partnering with DevAssist on the fully governed end-to-end developer experience.

*Our goal is simple:* Your teams shouldn't have to worry about databases at all. We'd love you to try it and give us feedback!

*IPS Team:* <@U03792RDPJ7|Aditya Patel> <@U07NA50FR61|Alex Stamenkovic> <@U08VAJQTJSD|Aman Singh Kaliyar> <@U06G14B0QN7|Amanjot Singh> <@W8FL45B7U|Andrew Bryndin> <@W8FL61BRQ|Andrew Chan> <@U048V9NBS5N|Arkaprabha Das> <@U02Q2V0CJDB|Arpit Agarwal> <@W8FQB4D0D|Ben Covi> <@W01620KJCBX|Bhavya Bordia> <@WJSN9F21H|Chanon Onman> <@W8F0R1HEU|Chau Nguyen> <@U08AHM96D2L|Crystal Ju> <@W9T6X9B0A|Daniel Russotto> <@U086R4YB6AC|Evan Tunstel> <@U051P9UBWMV|Girik Garg> <@W8FL39KM0|Gaurav Doon> <@W8FQB4R0D|Harshavardhan Srinivasan> <@U08QX7988CQ|Jesus Gonzalez> <@U05S25XEAVC|John Vargas> <@W8FMCE4EQ|Karan Seth> <@U02DX5VFX1V|Kaushik S> <@W8GN4EH0X|Larry Raab> <@U02T3RGSWSH|Matthew Smith (IPS)> <@W8FMA1KHS|Muthu Dakshinamoorthy> <@U01F1204RBN|Namrata Nerli> <@WB89HGUF9|Nancy Li> <@U0696AF757G|Nidhi Patel> <@W8FQB3CBF|Nishant Rangrej> <@U02SJP8LTFE|Niranjana H C> <@WAZ8C6KM3|Parthasarathy Sivasubramanian> <@WHELNUQ56|Ravi Kiran Vajepayayajula Venkata> <@W8GN4AF0X|Kiran Prasana> <@U02C7P858VD|Raj Parameswaran> <@U02QJGF8BDF|Sanket Bajoria> <@W8GG75DRU|Sandip Nahak> <@W019UEARUAZ|Sarathkumar Manoharan> <@W8FL3H59Q|Denson Pokta> <@W8FQCHV9B|Sohini S> <@U08EUKXAHME|Swapnil Bhargava> <@WC687HQ3X|Tanzeem Katmale> <@WAZRM3MN1|Tom Qian> <@WHNCG3F0T|Vineeth Kumar> <@U04UWGZEZMG|Vinod Ganapathy> <@U03EAUKJUCU|Wendy Wang>
*IPS Leadership:* <@W8FMAM7EY|Achal Kumar (858-200-6816)> <@W8GN4A3PZ|Tristan Baker> <@U02C7P858VD|Raj Parameswaran> <@WC687HQ3X|Tanzeem Katmale> <@U02DX5VFX1V|Kaushik S> <@U02QJGF8BDF|Sanket Bajoria> <@U02BVMLUQ2J|Ashish Page> <@W8F0SPCAC|Vamsee Reddy>.
*Cc:* <@U09BTDY2ZD1|Deepa Bajaj> <@U092QPP60G4|Fredrick Roberts> <@U08UECD6USE|Suneet Nandwani>
Reactions: +1 (1), rocket (2)



---

=== Message from Payton Camilli (W012EU6L7FG) at 2026-04-27 14:26:43 PDT === 
Message TS: 1777325203.368039
:airplane_arriving: *x290 Experiment Landed: Inline Contact Search in Audience* :airplane_arriving: 

:loom: *<https://www.loom.com/share/acdf7d043bd64b18a3431176dc2cd965|DEMO video!>*

:bar_chart: *Experiment Results* Apr 13 → Apr 23, 2026 (*11 Days*)
    ◦ Primary: 
        ▪︎ Campaign Creation Rate (within 7-day post-search):
            • +2.91% lift = :trophy: *Big, Clear Winner*
    ◦ Secondary 
        ▪︎ Email Create Rate
            • +0.06% (Flat)
        ▪︎ Avg. Email Creates per C1
            • -1.71% (Flat/slightly negative, _less important compared to email create rate_)
    ◦ Guardrail
        ▪︎ Payoff Complete Rate :white_check_mark: No harm
            •  +0.31% lift (significant)
Reactions: nice_ (7), money_mouth_face (3), drake_dancing (2), awesome (1), raised_hands (1)



---

=== Message from Margarita Caraballo (U02KJDT7YMT) at 2026-04-27 17:50:05 PDT === 
Message TS: 1777337405.301869
:star: :test_tube: *Email OTP Code at Account Activation* :test_tube: 

:sparkles: *Feature being experimented with:*
• *What did we test:* How would enabling the user to have an activation code _in addition to_ email activation link impact account activations?
• *Hypothesis:* Offering lower friction options for users to activate their account will result in a lift to account activations
• *Started:* April 2
:glasses: :chart_with_upwards_trend: *Learnings and Results* 
• +3.74% increase in account activation rate
• 33% decrease in session friction as measured by observing users being able to stay in the same browser session
<https://github.intuit.com/pages/Mailchimp-Analytics/product-analytics/experiment-readouts/otp_experiment_test/|Github dashboard>
<https://tableau.a.intuit.com/#/site/MChimp/views/IDOTPCodeResults/Dashboard1?:iid=1|Tableau dashboard>

:question2: *What’s Next*
We’re continuing to run this experiment to gain insights into whether there’s an impact to revenue and will be back to update! :salute-cat: 

:blessed2: *Huge props to the identity team and our partners for getting this out to customers*.
• TPM: <@U02KMDCS7PD|Lauren Ebrahim> <@U02KEEE7V8E|Chanel Hicks> 
• Product: <@U06QRS4SEBC|Rianna Schanno> <@U02KPFWHRU4|Elena Simon> 
• Eng: <@W8GN4BUBH|Danh Dang> <@W8FM8V11S|Jed Apostol> <@W9KGP4FM0|Alan Cruz> <@U02URC9KK46|Lawrence Ma> 
• Design: <@U02KM9USVDY|Greg Clark> <@U0A6NGFDM0V|Maya Pelichet> 
• Data Science: <@U03A5T1UH4M|Matthew Hendler> 
*Please feel free to reach out if you have any questions or thoughts.*
Thread: 2 replies (latest: 2026-04-28 07:17:42 PDT)
Reactions: cartwheel-freddie (6), raised_hands (1)



---

=== Message from Elizabeth Bertasi (U06QWR7FV9T) at 2026-04-28 06:45:20 PDT === 
Message TS: 1777383920.044159
:rocket: :cjb: :new: _*Now live: "Joins Segment" as a trigger in Automation Flows*_
We just shipped one of the most-requested capabilities in Mailchimp Automations — a huge step toward closing the competitive gap on automation flexibility.

:question: *What shipped?* A new _Joins Segment_ trigger that starts an automation when a contact enters segment the C1 has defined. No more manual tagging workarounds.

:target-4417: *Who it's for?* DSB and midmarket users on Standard+ plans. Especially powerful for HVCs who've been asking for precise segment-based triggers for years.

:chart-increasing: *Why it matters:*
• _Tag Added_ is the #2 most popular trigger today (26% of journeys) — a clear signal users want data-driven triggers but were stuck on workarounds
• Missing segmentation in automations contributed to ~10% of automations-related churned users and ~20% of churned revenue according to the 2023 HVC churn report
:unlocked-2: _Use cases unlocked are vast, including:_
Behavioral re-engagement when a contact enters a "no engagement in 30 days" segment
Follow-up when a contact has engaged with specific content in a window of time via a "Clicked link in last 7 days" segment
Send users who enter your VIP segment a thank you promo code

:thank_you: Huge thanks to the _Automations_, _CDP_, _Segmentation_ teams for the work that made this possible. :raised_hands:
Automations: <@U02KMBDS7AP|Heather Dartz> <@U02KJ1UDHC5|Bobby Craig> <@U03GVFDGUKA|Cliff Martin> <@U02KMGM5D98|Yena Ku (they-them)> <@U07UCSZSA30|Keith Ferney> <@U03GE2Y59M0|Dana Winn (Automations Oncall)> <@W0128TGRTDM|Erik Follette Romero> <@U02KJAK7GA1|James Moriarty> <@U02KZU660AV|Jameson Brown> <@U02KMC0QGSW|Justin E. Samuels> <@U02KMDU1TU2|Maxwell Reich> <@U07UY6KBVNV|Rob Berryhill> <@U07NA0QPYJ0|Saisharath Peddibotla> <@U09LKQLTUF4|Swati Pawar> <@U0AQYUMRLLE|Umesh Ravuru> <@U02P9STSQGZ|Becca Walsh> <@U02KJ5X1V3P|Cary Duncan> <@U04925BQ27M|Ade Ajanaku> <@U07RKQ1P8Q2|Yizhou Qiu>
CDP - StarRocks: <@W8FQBCLJH|Jake Hilborn> <@U04MT1U3MEJ|Caique Costa> <@U07GRQTTY30|Arkesh Rath> <@U077DQK10UA|Mohan Pandiyan> Enricher: <@U0751G9BR97|Philip Yin> <@U01J5GVP5GV|Kuntal Naphade> API: <@U04SC218QQ3|Sijia Liu> <@U08EGV08N4A|Alex Mitelman> <@U07146FU35X|Jeffrey Li>  MCS: <@W8FL3HEMQ|Navjot Cheema> <@U061WNX4T9T|Thomas Chen> EMs: <@U0789R246JY|Leila Jalali> <@U04QNS5KEE6|Ajeet Seenivasan> PM: <@U078B7PT3A8|Dan Damkoehler>
Segmentation: <@U03KUBTCSG1|Frank Persico> <@U07Q70L7BC5|Vova (Vladimir) Shechtman> <@U03FR4962NR|Russell Sidney> <@U03H4220CK0|Yoel Gonzalez> <@W8FJ04FH9|Andrei Khmelnitski> <@U07TY6D8Z0F|Brandon Culp> <@U09UQP5A3NH|Ermiyas Liyeh> <@U035AGFSBRC|Sabrina Harris>
Thread: 5 replies (latest: 2026-04-28 09:22:11 PDT)
Reactions: raised_hands (22), catjam (22), yay (17), rocker (13), lets_go (11), tada (7), rocket (8), raised_hands::skin-tone-3 (3), cat_clap (5), raised_hands::skin-tone-2 (4), raised_hands::skin-tone-4 (2)



---



# CHANNEL: #mc-experimentation-xfn

**129 top-level messages**

---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-08-04 08:47:06 PDT === 
Message TS: 1754322426.193729
Good morning team.
:alert:  Any experiments you all want to add to the Agenda for this week?
There were  two experiments (Task checklist and Optimizing import complete notifications) -  @Jennie Zhou - can you confirm if you'd like to keep that on the agenda?
If anyone else has upcoming experiments or recent concluded to share,  please add to the agenda by EOD today.

[End of channel history within window]


---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-08-04 10:50:43 PDT === 
Message TS: 1754329843.416939
8/5: Agenda 
- 11:05 PST: [Planning] Task Checklist EDD | Figma - @Andrew Spitz + Email (domain auth);  Integrations, Forms
- 11:20 PST: [Planning] Optimizing the import complete notifications to drive campaign creation EDD - @Andrew Spitz + Audience
:point_right: @Pratik Gupta/@Devin Mercier;  Integrations @Jason Cross, Forms @Matt Cimino, Audience @Amogh Mundhekar - I included you as the experiment may impact your areas.  Pls join or send a delegate. TIA!
Reactions: brat_ack_ty (1), thankyouuu (1)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-08-05 06:39:10 PDT === 
Message TS: 1754401150.728849
One additional topic for today  -->
- 11:35 PST:  [Results Readout] Leverage Builtwith Results and intent to ship - @Andrew Spitz + Audience @Amogh Mundhekar 



---

=== Message from Andrew Spitz (U08D0C42PJM) at 2025-08-05 09:10:42 PDT === 
Message TS: 1754410242.124759
hey @Phuong Trang is it possible to swap the ordering of the task checklist and the leverage builtwith results? Ideally Kateryna would be able to join and she's busy in interviews until 11:30



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-08-05 09:56:04 PDT === 
Message TS: 1754412964.533959
We can, but also want to be mindful should others had planned on dropping in during specific sessions.  The agenda update will be this --- does this work for folks?

- 11:05 PST: [Results Readout] Leverage Builtwith Results and intent to ship - @Andrew Spitz + @Amogh Mundhekar
- 11:20 PST: [Planning] Optimizing the import complete notifications to drive campaign creation EDD - @Andrew Spitz + @Amogh Mundhekar 
- 11:35 PST: [Planning] Task Checklist EDD | Figma - @Andrew Spitz + @Pratik Gupta/@Devin Mercier, @Amogh Mundhekar, @Matt Cimino,  @Jason Cross/@Ade Ajanaku 

Thread: 2 replies (latest: 2025-08-05 11:23:51 PDT)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-08-05 17:58:13 PDT === 
Message TS: 1754441893.912209
Thanks, team,  for joining our inaugural XFN Experiment Sync today!  :raised_hands:
Here is the Recording, Passcode: s7yB2a%+
(also linked in the agenda doc for easy access)

Reminder: This is your forum - not just for the Growth team.  If you have an upcoming or recently concluded experiments that impact multiple surfaces,  please:
- Signup here 
- Tag the relevant teams so we can align/send invite
Feel free to forward the weekly invite series or add your teams to this channel.  We'll use this slack channel to stay connected on agenda topics.  Thanks again!



---

=== Message from Amogh Mundhekar (WPDQYNNA0) at 2025-08-07 13:28:23 PDT === 
Message TS: 1754598503.282169
@Andrew Spitz - For the shopify cta experiment, if I heard you correctly in the program review today, it has a negative impact on C2 growth for FTUs but no harm for tenured users? Could you confirm, and let us know what release plan you have in mind?

cc @Payton Camilli
Thread: 1 replies (latest: 2025-08-07 13:55:08 PDT)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-08-11 08:58:29 PDT === 
Message TS: 1754927909.244949
:alert1:  Agenda - August 11
- 11:05 PST: [Planning]  x100 Streamline the Front Door for Omnichannel EDD | @Andrew Spitz + Automations, Forms, Email
- 11:20 PST: [Planning] x116 Increase visibility of contextual push to mobile EDD | @Andrew Spitz + Email
:point_right: @Rianna Schanno, @Matt Cimino, @Shruthilaya Jayabalan - I included you as the experiment may impact your areas.  Pls join or send a delegate.
Thread: 3 replies (latest: 2025-08-12 09:17:24 PDT)



---

=== Message from Nicole Jayne (U02LB4JPAEL) at 2025-08-14 07:38:38 PDT === 
Message TS: 1755182318.044509
Request: Could an account's assignment into the holdout group be sent into Amplitude as a user attribute we can all use to filter for users not eligible to see our experiences?
Thread: 9 replies (latest: 2025-11-05 10:55:13 PST)
Reactions: lookin (1)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-08-18 09:05:16 PDT === 
Message TS: 1755533116.928999
:alert1:  Agenda - August 19
- 11:05PST[Planning] xID201 New SMS Templates |  Figma | @Jeremiah Edmond 
- 11:35PST[Planning] New attribution defaults | EDD  | @Nicole Jayne 
:point_right: @Gary Aloisio. @Jeremy Diaz, @Aastha Sehgal, @Sarvesh Kumar - I included you as the experiment impact your areas.  Pls join or send a delegate.
Thread: 6 replies (latest: 2025-08-19 06:00:19 PDT)
Reactions: thanks-ty (4)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-08-19 07:55:31 PDT === 
Message TS: 1755615331.281419
Morning!  We have an additional topic for today at 11:20
:alert1:  Agenda - August 19
- 11:05PST | x201| New SMS Templates |  Figma | @Jeremiah Edmond
- :new: 11:20PST| x202| Email Image Size | EDD | @Devin Mercier 
- 11:35PST | xTBD | New attribution defaults | EDD  | @Nicole Jayne
:point_right: + @Heuisu Kim + @Joshua Fischer @Gary Aloisio. @Jeremy Diaz, @Aastha Sehgal, @Sarvesh Kumar - I included you as the experiment impact your areas.  Pls join or send a delegate.
Thread: 4 replies (latest: 2025-08-19 14:23:16 PDT)
Reactions: brat_ty (5)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-08-19 14:23:16 PDT === 
Message TS: 1755638596.168189
- :clapper: Today's zoom recording and passcode: 4%7dT4pJ.  Also linked in agenda doc
- Experiment tracker  - reminder to add your experiment into the tracker + include dates and surface.  This helps all squads to remain aligned and have a holistic Q1 overview of active, concluded + upcoming experiments.  TIA!
   - cc:  @Nicole Jayne, @Jeremiah Edmond, @Devin Mercier 
Reactions: thank_you_ty (2)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-08-25 08:24:24 PDT === 
Message TS: 1756135464.714859
:alert1:  Agenda - August 26
- 11:05 PST| x##| Email template gallery redesign | Email -  @Joshua Fischer 
- 11:20 PST| x##| Image Editing M1| Email - @Joshua Fischer 
:point_right:  + @Madeleine Stein, @Kevin Martin, @Ashley Wiesner - included you as the experiment impact your areas.  Pls join or send delegate
Thread: 1 replies (latest: 2025-08-27 07:52:22 PDT)



---

=== Message from Molly Hoffmeister (U02KPLF0PPW) at 2025-08-27 07:52:22 PDT === 
Message TS: 1756306342.134539
- :clapper: Zoom recording | Passcode: w^8.HytT (also linked in agenda doc)
- Experiment tracker - reminder to add your experiment into the tracker + include dates and surface :blob-thx:
Reactions: ty3 (2)



---

=== Message from Rianna Schanno (U06QRS4SEBC) at 2025-08-28 12:48:19 PDT === 
Message TS: 1756410499.700469
Hi yall! Not sure where to direct these suggestion but my team and I were chatting about opportunities with the Holdout Group.  Our team had some suggestion
- QA on Holdout Experience: Is there a regression or smoke testing process to ensure that the experience for Holdout group 
- MCAdmin or Amplitude Dashboard that shows the Holdout status for each C1.
- Prompt Product folks to LAU to ensure that they are doing Product validation for Holdout and non-holdout users
@Phuong Trang can you direct?

cc @Devin Mercier @Elizabeth Bertasi @Brittney Muhamed @Joshua Fischer @Halil Kiper
Thread: 5 replies (latest: 2025-09-02 08:20:19 PDT)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-09-02 08:24:04 PDT === 
Message TS: 1756826644.533699
<!here> - No signups in our agenda doc for today.  Please reply in :thread: if any of you have topics for today's  XFN experiment meeting.



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-09-08 07:42:50 PDT === 
Message TS: 1757342570.977749
We have three slots available for tomorrow.  Please sign up if there is an upcoming experiment that needs input or a results readout.



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-09-12 12:31:44 PDT === 
Message TS: 1757705504.107689
Happy Friday PM, UX, and DS team!
We've got 17 experiments live in production :rocket: — 3 weeks into the holdout refresh and only 6 weeks into FY26. Great momentum for learning
- :point_right: If your team has an upcoming multi-surface experiment or a readout to share, please sign up for next week's experiment review here
- Color coding: :large_blue_circle: Concluded | :large_green_circle: Running | :large_purple_circle: In dev/In design
cc:  @Nathan Bullock ^
Reactions: celebrate (1)
Files: image.png



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-09-15 12:15:41 PDT === 
Message TS: 1757963741.142119
Hi there.  We have two confirmed topics for tomorrow.  There's space for 1 more if anyone has an upcoming experiment or readout to share.    Don't be shy.

:alert1:  Agenda - Sept 16
- 11:05 PST| x211 Email Campaign jump-start | Growth @Andrew Spitz 
- 11:20 PST| x210| Consolidated contact import | Growth @Mac Dillard 
:point_right:+ Email team (@Devin Mercier, @Pratik Gupta, @Claudia Majors)  included you as the experiment impact your areas.  Pls join or send delegate +



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2025-09-18 06:00:08 PDT === 
Message TS: 1758200408.542439
[Weekly experiment review signup reminder]
Thread: 1 replies (latest: 2025-09-19 11:12:49 PDT)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-09-22 09:49:47 PDT === 
Message TS: 1758559787.080179
:mega:  Evolving the X-team Experimentation Op mech

Starting this week, our weekly x-team experimentation sync will evolve and include mandatory PMs POCs and product DS attending.   It will remain a working session for teams to share upcoming plans and results, with a few important additions.

Purpose of the forum
- :same_same: Proactively align on cross-team experiments and spot conflicts early
- :new: Every core product team experiment has a learning plan with DS sign-off
- :new: Reserve the last 15-20 mins to review upcoming experiments and releases by team/area

What to expect
- 45 min: Experiment readouts or reviews (teams continue to sign up here in advance)
- 15 min: Round-robin by team/area to review pipeline & next steps
- Pre-req: Q1 experiments added to the in product experiment tracker.  (Add Q2 plans when available)
- Prep: None beyond what you already have (PRD, EDD, Figma, etc.)
Please reach out to me, Diana, or Nathan if you have questions.



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-09-23 08:26:46 PDT === 
Message TS: 1758641206.993779
No experiments were added for today's sync, hence we will dive straight into team/area updates today.
:point_right: Product and Product DS POCs: please share latest experiment pipeline and next steps. Keep it high-level for this initial round. This is to orient your XFN peers and flag any questions or dependencies that need followup/support.

:alert1:  Agenda - Sept 23
- Round-robin by team/area: review pipeline & next steps



---

=== Message from Nicole Jayne (U02LB4JPAEL) at 2025-09-25 05:49:04 PDT === 
Message TS: 1758804544.153209
Hi experiment experts! :sos: I'm trying to figure out how to test when a user is bucketed into an Optimizely experiment (control or variant). The requirement I set was to bucket when a user lands on a specific page in the app and I don't have a good way to see that happen before we launch.

If you have tested Optimizely bucketing before, please speak up or point me toward a resource!



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2025-09-25 06:00:28 PDT === 
Message TS: 1758805228.478589
[Weekly experiment review signup reminder]



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-09-30 09:10:32 PDT === 
Message TS: 1759248632.883639
:alert1: Agenda - Sept 30
- 11:00 PST| x114 | CJB Automations Homepage results readout | @Elizabeth Bertasi 
- 11:15 PST| Round-robin: review pipeline & next steps



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2025-10-02 06:00:38 PDT === 
Message TS: 1759410038.919289
[Weekly experiment review signup reminder]



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2025-10-09 06:00:20 PDT === 
Message TS: 1760014820.495379
[Weekly experiment review signup reminder]



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-10-14 09:52:11 PDT === 
Message TS: 1760460731.867019
:alert1: Agenda - Oct 14
Time | xID| Topic |  Surface/Team | Driver
- 11:00 PST| x202 | Email - Image Normalization results readout | @Devin Mercier (he/him) 
- 11:15 PST| Round-robin by team/area: review pipeline & next steps
:point_right: Product and Product DS POCs: please ensure the tracker reflects latest status ahead of our meeting.   for round robin,  share latest experiment pipeline and next steps, specifically any flags/support you may need from XFN peers.



---

=== Message from Devin Mercier (he/him) (W0132PNAC9X) at 2025-10-15 08:29:46 PDT === 
Message TS: 1760542186.383749
@Phuong Trang - I am reaching out to identify the correct process for rolling out a super small quality of life improvement for customers to solve for some rage clicks the team was seeing in FullStory. This change allows them to edit the name of their email within the Nuni editor. See the demo here. This functionality does not exist today. We plan to launch this respecting the holdout group. Question: does something small like this require the whole EDD creation, experiment approval, results review process? cc: @San'Quan Prioleau @JB Lovell @Brian Fong @Nathan Bullock
Thread: 6 replies (latest: 2025-10-15 12:41:04 PDT)
Reactions: ty3 (2)
Files: demo_in-editor-campaign-renaming-2-short.gif



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2025-10-16 06:00:24 PDT === 
Message TS: 1760619624.964999
:experiment:  Please sign up here for an upcoming Tuesday XFN experiment review by Friday noon EST
- Three slots avail each week
- Tag the relevant teams or attendees to include in invite



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-10-20 10:59:46 PDT === 
Message TS: 1760983186.735419
There are two readout topics signed up for  for tomorrow.  No topic driver or team names added to signup sheet <@U07B5L5983F|Cassandra Marshall> and <@U02LB4JPAEL|Nicole Jayne> is that yours? (experiment ID 113 and ID60?)
• Conversion Insights dashboard
• Actionable Insights
cc:  <@U040C49798T|Stephen Yu>, <@U02KEHAB5U6|Claudia Majors>
Thread: 1 replies (latest: 2025-10-20 11:11:35 PDT)

---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-10-20 14:04:24 PDT === 
Message TS: 1760994264.749129
Confirming the agenda for tomorrow.
:mega: We still have one slot avail on agenda if any team has an upcoming planned test or a recently concluded test to share/discuss.
:point_right: *REMINDER* - Please take 5 minutes and ensure the tracker reflects the latest - update experiment status, dates, results, DS signoff,  etc before our meeting.  It will make for a smoother checkin --  <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=308731027#gid=308731027&fvid=1658562118|Experiment Tracker link filtered by team>. Thank you!

:alert1:<https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Agenda> *- Oct 21*
_*Time | xID| Topic |  Surface/Team | Driver*_
• 11:00 PST| x113 | Reporting & Analytics - Conversion Insights results | <@U02LB4JPAEL|Nicole Jayne> 
• 11:15 PST| x60 | Reporting & Analytics - Actionable Insights results | <@U06UL7W90LS|Vivian Wang> 
• 11:30 PST|  Round-robin by <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=308731027#gid=308731027&fvid=1658562118|team/area>: review pipeline & next steps



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2025-10-23 06:00:30 PDT === 
Message TS: 1761224430.349839
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-10-28 08:55:02 PDT === 
Message TS: 1761666902.937389
:point_right: *REMINDER* - Please take 5 minutes and ensure the tracker reflects the latest before our meeting.  It will make for a smoother checkin --  <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=308731027#gid=308731027&fvid=1658562118|Experiment Tracker link filtered by team>. Thank you!

:alert1:<https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Agenda> *- Oct 28*
_*Time | xID| Topic |  Surface/Team | Driver*_
• 11:00 PST| <https://docs.google.com/document/d/1C0_6PYJKAx1rVBaaOWL7b4rLTg4dNTt6MFDsCzl8Nf8/edit?tab=t.0#bookmark=id.ldkvhsaa54st|x203> | Email - Templates Gallery results & learnings | <@U07RNSH0256|Joshua Fischer> 
• 11:15 PST| <https://docs.google.com/document/d/1i9SsYfI14q7s_KHK1G3UTeiNOB3hhgFtUCqm0FH2JDQ/edit?usp=sharing|x101> | Integrations - No CC Standard Plan Trial  results & learnings | <@U085DCH3MCN|Josh Bernhard> 
• 11:30 PST|  Round-robin by <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=308731027#gid=308731027&fvid=1658562118|team/area>: review pipeline & next steps




---

=== Message from Experiment Review  (B09BHA86BUJ) at 2025-10-30 06:00:30 PDT === 
Message TS: 1761829230.829269
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-11-04 09:27:40 PST === 
Message TS: 1762277260.123849
:alert1:<https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Agenda> *- Nov 4*
_*Time | xID| Topic |  Surface/Team | Driver*_
• 11:00 PST| <https://docs.google.com/presentation/d/19BCHWRKh4m2FuV5GHljOxiXF76zKtOZ5XEe0kY0Hi6k/edit?slide=id.g3a004d89d92_0_0#slide=id.g3a004d89d92_0_0|x204> | OBX - Setup Checklist: Dismissable Actions & domain auth | <@U06QRS4SEBC|Rianna Schanno> 
• 11:15 PST|  Round-robin by <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=308731027#gid=308731027&fvid=1866695939|team/area>: review pipeline & next steps
:point_right: *REMINDER* - Please take 5 minutes and ensure the tracker reflects the latest before our meeting.  It will make for a smoother checkin --  <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=308731027#gid=308731027&fvid=1658562118|Experiment Tracker link filtered by team>. I,e:   we've had several recent concluded experiments, please update
• with results (win, lost, neutral)
• link to results file
• if winner,  indicate scale date target



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-11-04 15:26:13 PST === 
Message TS: 1762298773.963829




---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-11-04 15:33:44 PST === 
Message TS: 1762299224.228619
:thread: Latest status (as of today) - pls true up by Nov 6.  TY!
• 13 live and running in production
• 26 concluded experiments 
Thread: 1 replies (latest: 2025-11-04 15:35:51 PST)



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2025-11-06 06:00:22 PST === 
Message TS: 1762437622.908829
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite
Reactions: white_check_mark (1)



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2025-11-13 06:00:11 PST === 
Message TS: 1763042411.882919
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-11-13 17:11:22 PST === 
Message TS: 1763082682.142829
Confirming the agenda for tomorrow.  We have three concluded experiments where teams will be sharing the learnings.

:alert1:<https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Agenda> *- Nov 14*
_*Time | xID| Topic |  Surface/Team | Driver*_
• 10:05 PST| x217 | Email - STO v2.1:  *<https://docs.google.com/document/d/1uZsyKCHZ8aR2iJATAwreArXowZaBn7rSyvQJW8e3B7s/edit?tab=t.0#heading=h.4c40og9ra3k3|Results & Learnings>* | <@W0132PNAC9X|Devin Mercier (he/him)> 
• 10:20 PST| x215 | Integrations - Canva Image Sync UX Improvement: *<https://docs.google.com/presentation/d/1yhREjfd9NmGwurT1BwAr_-JE2z8yV0tS1MO2RP4CrUk/edit?slide=id.g3989cd7d89e_0_0#slide=id.g3989cd7d89e_0_0|Results & Learning>*<https://docs.google.com/presentation/d/1yhREjfd9NmGwurT1BwAr_-JE2z8yV0tS1MO2RP4CrUk/edit?slide=id.g3989cd7d89e_0_0#slide=id.g3989cd7d89e_0_0|s> | <@U02L0341LMP|Pratik Gupta>, <@U085DCH3MCN|Josh Bernhard> 
• 10:35 PST| x225 | R&A - Order Attribution new defaults & net to gross: *<https://docs.google.com/document/d/1njZcOxDnIbqIOWtYUAIhTEOrOvJ-h6I0aszx7hYS398/edit?tab=t.qxe0fuvfw8oq|Results & Learnings>* | <@U02LB4JPAEL|Nicole Jayne>, <@U0970UUFN80|Ashish Prakash>
• Round-robin by <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=308731027#gid=308731027&fvid=1658562118|team/area>: key call outs, review pipeline & next steps
Reactions: thanks-ty (2), ack (2)



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2025-11-20 06:00:20 PST === 
Message TS: 1763647220.449349
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2025-11-27 06:00:11 PST === 
Message TS: 1764252011.320899
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-12-01 08:54:32 PST === 
Message TS: 1764608072.882029
Welcome back team.  :fallen_leaf: :turkey-2:
<!here> - we have available slots on the agenda for tomorrow.  <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Sign up> to share a recent learning or to review an upcoming experiment
Thread: 3 replies (latest: 2025-12-02 09:14:31 PST)



---

=== Message from Taylor Mattson (U05AMM7NF5J) at 2025-12-01 09:16:43 PST === 
Message TS: 1764609403.093439
Hi! Is there an easy dashboard/way to see whether or not a C1 is in the global holdout group? I have Splunk access if that's helpful info for you. Our team was trying to spin up an easy dashboard for it but I think we had the wrong query. Thank you so much! :slightly_smiling_face:
Thread: 3 replies (latest: 2025-12-01 09:43:54 PST)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-12-02 09:50:40 PST === 
Message TS: 1764697840.369579
:point_right: Hi <!here> - Ahead of today's checkin, Please take 5 minutes and ensure the tracker reflects the latest before our meeting.  It will make for a smoother checkin --  <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=308731027#gid=308731027&fvid=1658562118|Experiment Tracker link filtered by team> (updates to status or dates).  TY!
• Experiments Currently Live:  14 
• Experiments Upcoming Launch (in dev):  14
Files: image.png (ID: F0A118E99V4, image/png, 221.2 KB), image.png (ID: F0A0WUEGA83, image/png, 204.6 KB)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-12-02 10:15:39 PST === 
Message TS: 1764699339.884749
:alert1:<https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Agenda> *- Dec 2*
_*Time | xID| Topic |  Surface/Team | Driver*_
• 11:00 PST| xID | Predictive Analytic  *|* <@U02LB4JPAEL|Nicole Jayne> and <@U08J8FFFVAL|Stam Paterakis>  --> feedback  and alignment needed from  `R&A, Automations, Segmentation` Product Mgrs and DS
• Round-robin by <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=308731027#gid=308731027&fvid=1658562118|team/area>: key call outs



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2025-12-04 06:00:13 PST === 
Message TS: 1764856813.055809
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-12-08 10:57:43 PST === 
Message TS: 1765220263.177879
We have one result readout from campaigns team tomorrow and there's still room on the agenda.
Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> if you have a result readout or upcoming experiment to share!



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-12-09 10:15:48 PST === 
Message TS: 1765304148.352019
:alert1:<https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Agenda> *- Dec 9*
_*Time | xID| Topic |  Surface/Team | Driver*_
• 11:00 PST| x216a | Campaigns - Subject Line A/B Testing Results & Learnings *|* <@W0132PNAC9X|Devin Mercier (he/him)>, <@U07RKQ1P8Q2|Yizhou Qiu> - <https://docs.google.com/document/d/1ZCRMtdjnGCII7FSiW62lvzbHUWr-vi77tqIlErAiFGk/edit?tab=t.0#heading=h.niryatmsthiy|EDD>, <https://docs.google.com/spreadsheets/d/13RMEjW5s4Up_PXgPvAKMYCfwUxne19CzfsGPa3ipS4s/edit?gid=0#gid=0|Experiment Results>
• Round-robin by <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=308731027#gid=308731027&fvid=1866695939|team/area>: key call outs
:point_right: *REMINDER* - Please take 5 minutes and ensure the tracker reflects the latest before our meeting.  It will make for a smoother checkin --  <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=308731027#gid=308731027&fvid=1866695939|Experiment Tracker link filtered by team>



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2025-12-11 06:00:18 PST === 
Message TS: 1765461618.676359
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-12-16 07:48:08 PST === 
Message TS: 1765900088.590519
Hi team - we have 3 topics today.

:alert1:<https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Agenda> *- Dec 16*
_*Time | xID| Topic |  Surface/Team | Driver*_
• 11:00 PST| `[Feedback]` Audience & Segmentation - Inline search <https://docs.google.com/document/d/1rRvr6olmHxOj8bt6QhnB9M8XMjN-3ehuc0rq3XgwDcQ/edit?tab=t.0|EDD> <@W012EU6L7FG|Payton Camilli>, <@U087Q34S3T6|AJ Hundal> 
• 11:15 PST| `[Feedback]` Audience & Segmentation - Import SMS numbers <https://docs.google.com/document/d/10HSaFgAXfCQ-PROCSMaJ073bbEbdBIiwQCRrm7lR2zo/edit?tab=t.0|EDD> <@W012EU6L7FG|Payton Camilli>, <@U087Q34S3T6|AJ Hundal> 
• 11:30 PST| `[Results & Learnings]` Help - PON Experiment v1 <https://docs.google.com/document/d/1_31ayjkgkM7XUmybYnEah2Hq7N3TmWrSgkgdVteklP4/edit?usp=sharing|EDD> & <https://docs.google.com/presentation/d/1AJUzCYnwhNu8oBvd2Iyi4fGaST7Bz2bnePGxMJ2AFME/edit?slide=id.g344e9ab28a6_0_345#slide=id.g344e9ab28a6_0_345|Results> <@U02VDMANQPL|Matt Bernstein>, <@U06EYRJLPMX|Vicki Borja Jennings> 
• Round-robin by <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=308731027#gid=308731027&fvid=1866695939|team/area>: key call outs




---

=== Message from Phuong Trang (U07TMNHQ20N) at 2025-12-16 08:51:24 PST === 
Message TS: 1765903884.824189
:point_right:  *REMINDER* - Please take 5 minutes and ensure the tracker reflects the latest before our meeting.  It will make for a smoother round robin checkin --  <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=308731027#gid=308731027&fvid=1866695939|Experiment Tracker link filtered by team>.  We don't need to go into details, rather just key call outs.

FYI - There's 20 active experiments live in production!
Files: image.png (ID: F0A4BGH9AD7, image/png, 65.9 KB)



---

=== Message from Alexandra Pappas (U05A4D12BT8) at 2025-12-17 07:34:28 PST === 
Message TS: 1765985668.479799
Hi all! Please check out our update below. We are looking forward to continuing to dive into experimentation in the New Year. Happy Holidays!
Reactions: raised_hands (1)



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2025-12-18 06:00:07 PST === 
Message TS: 1766066407.330159
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2025-12-25 06:00:10 PST === 
Message TS: 1766671210.643439
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2026-01-01 06:00:12 PST === 
Message TS: 1767276012.004699
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2026-01-05 09:03:08 PST === 
Message TS: 1767632588.955009
<!here> Welcome back and happy New Year, team! Hope everyone had a great recharge. Excited to see 30+ experiments now running in production :muscle:. We’ll be resuming our weekly cross-team experiment reviews tomorrow, and there’s still room on the agenda if you have learnings to share or an upcoming experiment to preview.
:point_right: *Sign up here:* _<https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|link>_
Looking forward to the insights and momentum ahead.



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2026-01-05 09:18:06 PST === 
Message TS: 1767633486.220749
<https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Agenda> *- Jan 6*
• 11:00 PST| `[Feedback]` |xTBD|  Agentic Content Blocks <https://docs.google.com/document/d/1o5k4ZSMUYK08J2i6bDHyq2JD4nL-JvIioMyKPbO9Cow/edit?usp=sharing|EDD> <@U09979JPH37|Ose Amiegheme>, <@U085FK1578R|Bilel Bouraoui> 
• 11:15 PST| `[Feedback]` |x259 | Convert Email Content to SMS <https://docs.google.com/document/d/1KVsE7--OcZhdN9PXfSEdsQ8mvn-1Nh4pzSCbYtasXUA/edit?usp=sharing|EDD> <@U02KPE15PCL|Connor Callahan>, <@U085FK1578R|Bilel Bouraoui> 




---

=== Message from Nicole Jayne (U02LB4JPAEL) at 2026-01-07 10:32:42 PST === 
Message TS: 1767810762.182509
Hi! What's the plan to ending the H1 holdout group and reshuffling? We have many experiment launching end of Jan and wrapping by Feb 9.
Thread: 2 replies (latest: 2026-01-09 10:10:31 PST)
Reactions: eyes (1)



---

=== Message from Andrew Hessert (U089YD7EQDS) at 2026-01-07 13:56:59 PST === 
Message TS: 1767823019.848579
Hi :wave: we provided some guidance on experiment QA below. Check it out :exclamationn:
Reactions: ty-thanks (1)



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2026-01-08 06:00:16 PST === 
Message TS: 1767880816.133049
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Joshua Fischer (U07RNSH0256) at 2026-01-08 09:52:59 PST === 
Message TS: 1767894779.432449
If anyone else is using internal_mc_user=false  in their amplitude dashboard to exclude internal users, I recently discovered that was excluding about half of the external users in my experiment who had internal_mc_user="".
Reactions: white_check_mark (1)



---

=== Message from Devin Mercier (he/him) (W0132PNAC9X) at 2026-01-08 10:22:51 PST === 
Message TS: 1767896571.297779
ooh i have definitely used that before!



---

=== Message from Devin Mercier (he/him) (W0132PNAC9X) at 2026-01-08 10:23:08 PST === 
Message TS: 1767896588.782989
so we should instead be using is internal_mc_user=false OR ""



---

=== Message from Joshua Fischer (U07RNSH0256) at 2026-01-08 10:26:14 PST === 
Message TS: 1767896774.358919
This seems like it could be a bigger issue.  These "" users also don't have values for other fields like account_activation_timestamp or plan_type in Amplitude
 <https://app.amplitude.com/analytics/intuit-portfolio/chart/new/763ed3us?source=copy+url>



---

=== Message from Alexandra Pappas (U05A4D12BT8) at 2026-01-08 10:53:54 PST === 
Message TS: 1767898434.442709
Hi <@U07RNSH0256|Joshua Fischer> Thanks for flagging! We'll take a look and let you know what we find.
Thread: 6 replies (latest: 2026-01-09 08:18:45 PST)



---

=== Message from Jenn Reed (U02KEKMTNNA) at 2026-01-08 14:55:40 PST === 
Message TS: 1767912940.314149
Cross-posting for awareness! Please reach out in <#C03TH2L4QA1|mc-experimentation-support> if you have questions or need assistance.
Reactions: tybw (3)



---

=== Message from Jenn Reed (U02KEKMTNNA) at 2026-01-09 13:45:09 PST === 
Message TS: 1767995109.854269
Cross-posting here for visibility! Please reach out in <#C03TH2L4QA1|mc-experimentation-support> if you have any questions. Have a great weekend!
Reactions: tybw (1)



---

=== Message from Chethana V P (U086AEY40BF) at 2026-01-09 16:19:32 PST === 
Message TS: 1768004372.843169
*_[Experiment Launch]_ Mailchimp Left Navigation Information Architecture (aka Wayfinding Milestone 1)*
• _Launch Date: Dial-up starting 1/20 (Milestone 1a - first round of experiment for new customers) and 2/16 (Milestone 1b - second round of experiment for new and existing customers). Even though the first round is a week from now, we are posting details in advance for all Mailchimp domain teams to review and align with the changes._
• _Hypothesis:_ If we introduce a clearer, more predictable hierarchical nav structure, where users can see all major tools grouped under intuitive parent categories then they will more easily find and complete high-value actions (HVAs), because the nav will better match marketer mental models and reduce friction caused by hunting or unnecessarily clicking for features.
• _Metrics:_
       _Primary:_ High-Value Action (HVA) Completion — 14/30 Day (1+ and 2+ HVAs per user). Includes: Email send, Automation start, SMS send
      Guardrail Metric (Do No Harm) - Email Sends — 14-Day
      High visibility/priority metric (used for potential trade-off decision post experiment): SMS penetration rate
      Overall 12 secondary metrics (including wayfinding CSAT KPI) will be monitored closely to assess the impact on individual domains in order to perform iterative changes as needed.
• _Resources:_ <https://docs.google.com/document/d/13oDb4mzmjwLsfPL3OGZ8K7wNWRhoV0b_YSWTLVxU0kE/edit?tab=t.0|EDD> / <https://www.figma.com/design/PKzV6j5FhyHWksBRzrl1Hg/Mailchimp-Wayfinding-%E2%80%94-FY26?node-id=1-29&t=wzEOfGnIE7OdPKh3-1|Figma> / <https://docs.google.com/presentation/d/1l8YvyHZPGgr87C-GHsGVNUanaxivXIO08T-mjUDMPp8/edit?slide=id.g2ef4b94ff44_0_47#slide=id.g2ef4b94ff44_0_47|UXR findings> / <https://docs.google.com/presentation/d/1kpmkeEkoJXzm1GacM_OYjjcVongYSWxr4FBdkB51xKU/edit?slide=id.g369dffd4708_0_383#slide=id.g369dffd4708_0_383|High Value Actions>
Cc - <@U03DRMGVA1L|Mary McKeon> <@U06K8UTTSJE|Jing Wang> <@U02L01PENRF|Mark Maynard> <@U02LB7537J4|Zac Wall> <@U049ALKN4RK|Bethany Hodd> <@U060RFM8D27|Kranthi>
Thread: 1 replies (latest: 2026-01-09 16:39:09 PST)
Reactions: thanks-ty (1), raised_hands (1)
Files: Wayfinding Exploration (ID: F0A43CLEJE7, application/vnd.google-apps.presentation, 0 Bytes), <First draft> Experiment Design Doc – Mailchimp Left Navigation Information Architecture (Phase 1) (ID: F0A2SFBCNKU, application/vnd.google-apps.document, 0 Bytes)



---

=== Message from Jenn Reed (U02KEKMTNNA) at 2026-01-12 13:53:11 PST === 
Message TS: 1768254791.693249
Cross-posting here for visibility! Please reach out in <#C03TH2L4QA1|mc-experimentation-support> if you have any questions. :ty_:
Reactions: fire (1), thanks-ty (1)



---

=== Message from Alexandra Pappas (U05A4D12BT8) at 2026-01-12 13:55:41 PST === 
Message TS: 1768254941.955199
:exclamation:Hi! Please read through our update on when the Global Holdout will be refreshed below.:exclamation:
Reactions: raised_hands::skin-tone-3 (1), thanks-ty (1)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2026-01-12 16:51:28 PST === 
Message TS: 1768265488.241139
:blue_siren:  <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Agenda> *- Jan 13*
• 11:00 PST| `[Feedback]` |x265|  HTML > Nuni Email Design Converter <https://docs.google.com/document/d/1RsqI_BC5GYOlPqiBRF7NSPr7K0HC3E06Rd0z0MGyyN4/edit?tab=t.0#heading=h.etuyio6mi4qp|EDD> <@U07RNSH0256|Joshua Fischer>, <@U02R9QUKXUL|Shakib Ahmed> 
• 11:15 PST| `[Results & Learning]` |x264|HAO Left Panel <https://docs.google.com/document/d/1wIWQNZYdWucsDzRwMgXKqOuPmLiGr-lNGThfIW97hPI/edit?tab=t.0#heading=h.etuyio6mi4qp|EDD> <@U07RNSH0256|Joshua Fischer>, <@U02R9QUKXUL|Shakib Ahmed> 
• 11:30 PST| `[Feedback]` |xTBD| Wayfinding - Left Nav Architecture Milestone 1 <https://docs.google.com/document/d/13oDb4mzmjwLsfPL3OGZ8K7wNWRhoV0b_YSWTLVxU0kE/edit?tab=t.0#heading=h.43hdujvcolj5|EDD> <@U086AEY40BF|Chethana V P>, <@U02R9QUKXUL|Shakib Ahmed> 




---

=== Message from Jenn Reed (U02KEKMTNNA) at 2026-01-13 15:45:12 PST === 
Message TS: 1768347912.048479
Cross-posting update here for visibility! Please reach out in <#C03TH2L4QA1|mc-experimentation-support> if you have any questions. :thank_you-5899:
Reactions: tybw (1)



---

=== Message from Alexandra Pappas (U05A4D12BT8) at 2026-01-14 06:00:18 PST === 
Message TS: 1768399218.332589
Hi! We are shifting our Office Hours for the <https://intuit-teams.slack.com/archives/C03TD1T7DP0/p1768245183260269|Global Holdout Refresh> to 2:30 pm ET today due to the Mailchimp January Huddle. Please join us at <https://intuit.zoom.us/j/99629305725?pwd=XouDjnGzXZAz8TXAAVWYytpdmunUY2.1|this link> and feel free to sign up <https://docs.google.com/spreadsheets/d/1FBU1C45PWgUrB7uda664Uqfb8QSoxVOIgnvjdJUgryE/edit?gid=0#gid=0|here> in advance. As a reminder, we’ll be holding these weekly over the next four weeks. Thanks!



---

=== Message from Jenn Reed (U02KEKMTNNA) at 2026-01-14 14:25:48 PST === 
Message TS: 1768429548.575709
Daily update on Internal Account issues/feedback for today. Please reach out in <#C03TH2L4QA1|mc-experimentation-support> if you have any questions. :thanks-ty:
Reactions: tybw (1)



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2026-01-15 06:00:10 PST === 
Message TS: 1768485610.605779
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Jenn Reed (U02KEKMTNNA) at 2026-01-15 15:15:30 PST === 
Message TS: 1768518930.246029
Cross-posting for visibility! Now that they top priority requests have been completed, we'll move our status cadence from daily to weekly, and share our next update at the end of next week.

Please post any questions in <#C03TH2L4QA1|mc-experimentation-support>, thank you!
Reactions: thankyou1 (2), super-this (2)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2026-01-20 06:35:09 PST === 
Message TS: 1768919709.906529
:blue_siren:  <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Agenda> *- Jan 20*
• 11:05 PST| `[Results & Learning]` |  KB Article Recommender  <https://docs.google.com/document/d/1S_S0mq3jcSZHduV-ML0DZqw6G8oHTWGI41nbYcBqpow/edit?tab=t.0#heading=h.4c40og9ra3k3|EDD> & <https://docs.google.com/presentation/d/1vsiyKcxdfHo4KAASGQu4zWslTw6S5J3hbUkfPC2KcKw/edit?usp=sharing|Deck> <@U02VDMANQPL|Matt Bernstein>, <@WH2NN5N3C|Matthew Knell> 

Thread: 2 replies (latest: 2026-01-20 07:54:55 PST)



---

=== Message from Matt Bernstein (U02VDMANQPL) at 2026-01-20 07:49:52 PST === 
Message TS: 1768924192.936739
Discussed with <@U07TMNHQ20N|Phuong Trang> - going to give this time back and share a written summary here !
Reactions: white_check_mark (1), thanks-ty (1)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2026-01-20 07:54:55 PST === 
Message TS: 1768924495.624209
Thanks <@U02VDMANQPL|Matt Bernstein>.    Today's meeting is canceled and we will resume next week.  Lot's of <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=2032971585#gid=2032971585|experiment live> in production.   Please be sure to sign up for an <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|upcoming shareout here>



---

=== Message from Alexandra Pappas (U05A4D12BT8) at 2026-01-20 08:20:08 PST === 
Message TS: 1768926008.317909
:remind: Hi. A friendly reminder that we’ll be refreshing the Global Holdout later this week on 1/22. Please review our previous communications<https://intuit-teams.slack.com/archives/C03TD1T7DP0/p1768245183260269| here> and if you have any questions, please feel free to reach out in <#C03TH2L4QA1|mc-experimentation-support> or attend office hours tomorrow at 1pm ET. Please join us at this <https://intuit.zoom.us/j/99629305725?pwd=XouDjnGzXZAz8TXAAVWYytpdmunUY2.1|link> and feel free to sign up <https://docs.google.com/spreadsheets/d/1FBU1C45PWgUrB7uda664Uqfb8QSoxVOIgnvjdJUgryE/edit?gid=0#gid=0|here> in advance. Thanks!



---

=== Message from Matt Bernstein (U02VDMANQPL) at 2026-01-21 11:34:45 PST === 
Message TS: 1769024085.926099
:thread:KB Article Recommender <https://docs.google.com/document/d/1S_S0mq3jcSZHduV-ML0DZqw6G8oHTWGI41nbYcBqpow/edit?tab=t.0#heading=h.4c40og9ra3k3|EDD> & <https://docs.google.com/presentation/d/1vsiyKcxdfHo4KAASGQu4zWslTw6S5J3hbUkfPC2KcKw/edit?usp=sharing|Deck>

*Takeaway:* ECS can now be viewed as a valid source of signal for real-time AI/ML use cases (details in thread)
Thread: 1 replies (latest: 2026-01-21 11:35:47 PST)
Reactions: ty3 (1)



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2026-01-22 06:00:10 PST === 
Message TS: 1769090410.318569
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Andrew Hessert (U089YD7EQDS) at 2026-01-22 12:12:33 PST === 
Message TS: 1769112753.143499
:refresh-5740: The Global Holdout has been refreshed :refresh-5740: :party:

Please make sure all experiments launched going forward use the FY26*H2* Holdout. Thanks all :slightly_smiling_face: :rocket:
Reactions: ty3 (2), +1 (1), +1::skin-tone-2 (1)



---

=== Message from Jenn Reed (U02KEKMTNNA) at 2026-01-23 14:03:46 PST === 
Message TS: 1769205826.280409
:fyi-8599: All internal account issues/requests have been resolved. Just sharing for visibility. :slightly_smiling_face:



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2026-01-26 10:44:14 PST === 
Message TS: 1769453054.334369
Hi team - ~we have room on the agenda for tomorrow if you have upcoming experiments or results to share.~
_(additional readout added to agenda)_

:blue_siren:  <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Agenda> *- Jan 27*
• 11:05 PST| `[Results & Learning]` | Marketing Landing page to drive MC attach in Fusion <https://docs.google.com/document/d/1GjPNWBxLoiRWAT5Xr4Ka7wLyVX1su3cyhXwtdX73S7c/edit?tab=t.0#heading=h.xpwclgox6ixz|EDD> <@U03AME5740K|Chima Okechukwu> <@U0928GRQ65V|Luke Puglisi> 
• 11:20 PST| `[Results & Learning]` | x236: Setup homepage checklist <https://docs.google.com/document/d/17lw4XAvHJlXU2DNQD3hAQ62is6XL9o5druBNKRCIseg/edit?tab=t.7xhw4pg6heg8#heading=h.4c40og9ra3k3|EDD> <@U09LX79M6HJ|Eva Frishberg> <@U02R9QUKXUL|Shakib Ahmed> 
• 11:35 PST| `[Results & Learning]` | x254: Progress Indicator in Email Checklist <https://docs.google.com/document/d/1sipoUOL5gYWyZPlM4_ljSEKoczIVHAhOHMez0eh8-D4/edit?tab=t.0#heading=h.4c40og9ra3k3|EDD> <@W0132PNAC9X|Devin Mercier (he/him)> <@U07RKQ1P8Q2|Yizhou Qiu> 



---

=== Message from Alexandra Pappas (U05A4D12BT8) at 2026-01-27 06:44:51 PST === 
Message TS: 1769525091.181319
:rocket: *Join the IXP Experimentation Pilot* :rocket:

Hi Product Managers! Starting in <https://intuit-teams.slack.com/archives/C03TD1T7DP0/p1765985410060629|March>, we will be transitioning to *IXP* as our required experimentation platform. To ensure a smooth transition, we are launching an *Experimentation Pilot.* We're looking for volunteer teams to run an experiment with us on IXP in the next few weeks. If you have an upcoming launch, please reach out!!!

Joining the pilot gives your team the advantage of onboarding early with hands-on support from both the IXP Platform and Mailchimp Experimentation experts. To ensure that everyone in the pilot feels prepared, we'll be hosting a dedicated training session for teams and will be available every step of the way.

*What this means for you:*
• *Product Managers & Data Scientists:* The training and pilot will guide you through the new change management processes with expert oversight.
• *Engineers:* The transition is straightforward—the primary shift is leveraging the IXP wrapper in your code rather than the Optimizely wrapper.
If you’re interested in getting a head start and shaping our experimentation culture, please let me know by the end of the day tomorrow (1/28)! Feel free to reach out with any questions.
Reactions: super-this (2)



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2026-01-29 06:00:26 PST === 
Message TS: 1769695226.196839
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2026-02-02 11:59:50 PST === 
Message TS: 1770062390.297549
Hi team - there's room on the agenda tomorrow if you have a topic to share.

:blue_siren:  <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Agenda> *- Feb 3* 
11:05 PST| `[Results & Learning]` | x236: Setup homepage checklist <https://docs.google.com/document/d/17lw4XAvHJlXU2DNQD3hAQ62is6XL9o5druBNKRCIseg/edit?tab=t.7xhw4pg6heg8#heading=h.4c40og9ra3k3|EDD> <@U09LX79M6HJ|Eva Frishberg> <@U02R9QUKXUL|Shakib Ahmed> cc: <@U08D0C42PJM|Andrew Spitz>



---

=== Message from Yizhou Qiu (U07RKQ1P8Q2) at 2026-02-03 09:41:45 PST === 
Message TS: 1770140505.893179
Hi team, wondering where I can find the list of user_ids that were included in the H1 holdout group.
Thread: 3 replies (latest: 2026-02-03 10:12:14 PST)



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2026-02-05 06:00:02 PST === 
Message TS: 1770300002.786619
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite
Thread: 1 replies (latest: 2026-02-06 14:54:30 PST)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2026-02-09 17:23:31 PST === 
Message TS: 1770686611.027669
:blue_siren:  <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Agenda> *- Feb 10* 
• 11:05 PST| `[Results & Learning]` | x259 and x280:  Email to SMS Report <https://docs.google.com/document/d/1KVsE7--OcZhdN9PXfSEdsQ8mvn-1Nh4pzSCbYtasXUA/edit?tab=t.0#heading=h.4c40og9ra3k3|EDD> <@U02KPE15PCL|Connor Callahan> 
• ~11:20 PST| `[Feedback]` | x357 FOMO in free - referral badge <https://docs.google.com/document/u/0/d/11vVOLy8KjDtH7d7Bhv3jQwU8JMuYJieCcoeHu38dXA0/edit|EDD>~ ~<@U08N2BTNV46|Jennie Zhou>~ 
cc:  <@U085FK1578R|Bilel Bouraoui> <@U02KM1TUH8B|Ashley Lawrence> <@U03BZL23C1F|Heuisu Kim> <@U02KPLF0PPW|Molly Hoffmeister> <@U09979JPH37|Ose Amiegheme> <@U02KM32BC67|Alejandra Rodriguez> <@U06QRS4SEBC|Rianna Schanno>
Thread: 2 replies (latest: 2026-02-10 08:45:39 PST)



---

=== Message from Gary Aloisio (U0703THQZRQ) at 2026-02-10 07:08:37 PST === 
Message TS: 1770736117.752739
I have some questions about creating an experiment from scratch and some of the fields for experiment creation using IXP for Mailchimp SMS. Is anyone available for about 15 mins for a quick walkthrough?
Thread: 3 replies (latest: 2026-02-10 07:40:07 PST)
Reactions: resolvedhappy (1)



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2026-02-12 06:00:14 PST === 
Message TS: 1770904814.842549
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2026-02-12 16:22:16 PST === 
Message TS: 1770942136.553489
Sharing <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|agenda> for next week early as I will be on PTO next Tuesday.

:blue_siren:<https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|  Agenda> *- Feb 17*
• 11:05 `[Results]` New Shopify Triggers <@U06QWR7FV9T|Elizabeth Bertasi> 
• 11:20 `[Feedback]` Email Easy Template <@U03AME5740K|Chima Okechukwu> 
:point_right:  If you have additional topics (we have room)  please add to the <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|signup sheet> and let <@U02KEHAB5U6|Claudia Majors> know.  TIA Claudia and <@W8F0RNH4Y|Nathan Bullock> for running next week's meeting!

cc:  <@U093KFQ7D9U|Monique Parnell>



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2026-02-19 06:00:22 PST === 
Message TS: 1771509622.720019
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2026-02-23 17:44:13 PST === 
Message TS: 1771897453.961849
:blue_siren:<https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|  Agenda> *- Feb 24*
• 11:05 PST `[Results & Learning]` xTBD | Email - Font Picker   <@U09979JPH37|Ose Amiegheme> <@U02QFTEHKB9|Kevin Martin> 
• 11:20 PST `[Feedback]`  x337 | Pickup Where You Left Off *<https://docs.google.com/document/d/1L36mbGrpNw9aakXIVpZOlGm1yrIe3DQoP0R6_2hSMR4/edit?tab=t.0|EDD>* <@U07RNSH0256|Joshua Fischer> <@U086AEY40BF|Chethana V P> 
• 11:35 PST `[Feedback]`  x250 | MC Sandbox Capability *<https://docs.google.com/document/d/1Frtqnv9CjgNciEoBOUDb1iZsKGqfUQwEyPFDN-RJkig/edit?tab=t.xprftjbqo0b9|EDD>* <@U08D0C42PJM|Andrew Spitz> <@U09FQRBQSRF|Lucas Ruprecht> 



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2026-02-26 06:00:16 PST === 
Message TS: 1772114416.670279
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from slackbot (B01) at 2026-02-26 13:58:24 PST === 
Message TS: 1772143104.793389
<@U03BP6T1BT6|Slack App Service Account> has added *<#C095TT75VTQ|mc-experimentation-xfn>* to *Intuit Slack Connect*, another *Intuit* workspace using the channel management tool. Any member of that workspace can now find and join this channel.  <https://slack.com/trust/data-management|Learn more>.



---

=== Message from Slackbot (USLACKBOT) at 2026-02-26 14:02:21 PST === 
Message TS: 1772143341.096419
*charles* from *Irrational Labs* was added to this channel by *cgreen16*. You can review their permissions in Channel Details. Happy collaborating!



---

=== Message from Alexandra Pappas (U05A4D12BT8) at 2026-03-03 07:49:11 PST === 
Message TS: 1772552951.325369
Cross-posting the latest capability updates on experimentation
Reactions: raised_hands::skin-tone-3 (1), raised_hands (1), woo_hoo (1)



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2026-03-05 06:00:25 PST === 
Message TS: 1772719225.587419
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Nicole Jayne (U02LB4JPAEL) at 2026-03-05 10:07:02 PST === 
Message TS: 1772734022.643639
Hello! We are diagnosing why our Marketing Dashboard and Predictive Analytics cohorts are so heavily skewed/imbalanced on many C1 dimensions.

Does anyone have a recent experiment that was bucketed at landing on an interior page? Anything NOT bucketed at login?
Thread: 3 replies (latest: 2026-03-06 05:24:32 PST)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2026-03-09 09:45:41 PDT === 
Message TS: 1773074741.301929
:blue_siren:<https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|  Agenda> *- March 10*
• 11:05 PST `[Results & Learning]` x381 | Audiences & Segmentation: All Contacts zero state <https://docs.google.com/document/d/1lRVdtWqezp3wyRBCGgA_bi52bPH6srNXyQyZG0OXUWk/edit?tab=t.0#heading=h.4c40og9ra3k3|EDD> <@U02KZL81PLH|Caroline Ramirez> <@U08CE9D9QKS|Patrick Kopps> 
• 11:20 PST `[Feedback]`  x399 | Support: Assistant FAB Scale <https://docs.google.com/document/d/1gASfZnoBrnH2b_HWgbkRDVS1Nzf-Ii_qRusGh3KHJLQ/edit?tab=t.0#heading=h.fgf05bbrjqr|EDD> <@WH2NN5N3C|Matthew Knell> 
• 11:35 PST `[Feedback]`  x401 | Support: Webinar Entry Point in Help Panel <https://docs.google.com/document/d/1bMfTCz8CYn2fmkLMtJyJfRMbD0NI83S5puZ8IaScF-s/edit?tab=t.0#heading=h.fgf05bbrjqr|EDD> <@WH2NN5N3C|Matthew Knell> 



---

=== Message from Alexandra Pappas (U05A4D12BT8) at 2026-03-11 09:08:37 PDT === 
Message TS: 1773245317.382799
Hi! Please find our newly released milestones for the upcoming transition from Optimizely to IXP for experimentation and feature flags.



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2026-03-12 06:00:20 PDT === 
Message TS: 1773320420.198759
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2026-03-16 14:39:25 PDT === 
Message TS: 1773697165.149989
:blue_siren: <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Agenda> *- March  16*
• 11:05 PST `[Results & Learning]`x372 No CC Trials v2  <http://x372%20No%20Credit%20Card%20Required%20Trials%20V2%20-%20Experimentation%20Design%20Doc|EDD> <@U08N2BTNV46|Jennie Zhou> <@U02LARVGVGQ|Amanda Hunt> <@U02ATLVNQCV|Hrishikesh Babar> <@U09C3GFP1PU|Minori Jaggia> 
:point_right:  PM/DS leads <@U06QRS4SEBC|Rianna Schanno> <@U02KJEHK677|Neil Desai> <@U09979JPH37|Ose Amiegheme> <@U08DYEMBSSG|Jason Cross> <@U079SMT5UTA|Matt Cimino> <@U02KEHAB5U6|Claudia Majors> <@U0970UUFN80|Ashish Prakash> - flagging as this may impact your area

Open slots available.  Bring an upcoming experiment or a recent learning to share.  Drop a reply :thread: or DM me to grab a spot.



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2026-03-19 06:00:11 PDT === 
Message TS: 1773925211.099749
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Andrew Hessert (U089YD7EQDS) at 2026-03-19 11:53:41 PDT === 
Message TS: 1773946421.267009
Hi Friends :wave:  Please see our <https://intuit-teams.slack.com/archives/C03TH2L4QA1/p1773946062334809|post-incident update> for summarizing experimentation impact. TY!
Thread: 3 replies (latest: 2026-03-20 10:33:19 PDT)
Reactions: thank_you-5899 (1)



---

=== Message from Alexandra Pappas (U05A4D12BT8) at 2026-03-20 11:27:44 PDT === 
Message TS: 1774031264.691439
Please see below for an update on recent exclusions from the Global Holdout.



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2026-03-23 13:27:05 PDT === 
Message TS: 1774297625.203609
:blue_siren: <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Agenda> *- March  24*
We have three `[Results & Learning]`  tomorrow
• 11:05 PST  x374 | OBX Streamline GTKM OBS Experiment *<https://docs.google.com/document/d/1N3u5kTg__ZjUovwdTH3vDY2ZgJ7OxGEJiz6j1ZSCRaM/edit?tab=t.0#heading=h.xpwclgox6ixz|results> & <https://docs.google.com/document/d/1x0DJWR7-ozN6eAmEYxTTwrCTutfatHCMjDWSRDGfqHQ/edit?tab=t.0|EDD>*  <@U06QRS4SEBC|Rianna Schanno> <@U07UCMXJNPP|Jeevisha Anandani> 
• 11:20 PST x373 | Integrations CTA on Revenue in ACP <@U085DCH3MCN|Josh Bernhard> <@U099JC6013K|Prasad Sawant> 
• 11:35 PST x406 | OBX MAB for OBS Checklist *<https://docs.google.com/document/d/1N3u5kTg__ZjUovwdTH3vDY2ZgJ7OxGEJiz6j1ZSCRaM/edit?tab=t.0#heading=h.xpwclgox6ixz|EDD>* <@U07RNSH0256|Joshua Fischer> <@U02VDMANQPL|Matt Bernstein> 

Thread: 2 replies (latest: 2026-03-24 10:10:47 PDT)
Reactions: thank_you (1)



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2026-03-26 06:00:08 PDT === 
Message TS: 1774530008.819009
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2026-03-30 15:59:50 PDT === 
Message TS: 1774911590.435389
:blue_siren: <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Agenda> *- March  31*
• 11:05 PST x369 | [Results] SMS Templates in Unified Temp Gallery <https://docs.google.com/document/d/1mvhthB1WxWfv-Hz9x9FnP-O6kfVNMGG_S_57yWAaB4Q/edit?tab=t.0#heading=h.4c40og9ra3k3|EDD> <@U09979JPH37|Ose Amiegheme> 
• 11:20 PST x373 | [Results] Integrations CTA on Revenue in ACP <https://docs.google.com/document/d/1Te1aNjn3UPvYgoD5YN8FY5vPHlyF1m4bLFDyvTVp8-A/edit?tab=t.0#heading=h.xpwclgox6ixz|EDD>  <@U085DCH3MCN|Josh Bernhard> <@U099JC6013K|Prasad Sawant> 
• 11:35 PST x267 | [Feedback]  Branded Templates <https://docs.google.com/document/d/1655OY1beT0Pg9vVIW1IzbmWrpYoy0ph4jhs2rjSigLY/edit?usp=sharing|EDD> <@U09979JPH37|Ose Amiegheme> 

Reactions: +1 (1)



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2026-04-02 06:00:10 PDT === 
Message TS: 1775134810.629969
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Alexandra Pappas (U05A4D12BT8) at 2026-04-03 05:48:53 PDT === 
Message TS: 1775220533.382329
:announcement-loud: Here is the summary and resources for our IXP Onboarding sessions this week. Please don't hesitate to reach out with questions!
Reactions: thankyou1 (1)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2026-04-03 11:15:37 PDT === 
Message TS: 1775240137.075699
Hello team!  If you weren't able to join the IXP sessions this week,  please make time to view the recording and deck <@U05A4D12BT8|Alexandra Pappas> shared.  And take note of the following dates so you can plan accordingly!

> :'arrow: :date: Coming Up: IXP Open for Everyone
> As a reminder, IXP will be open for all new experiments starting *`April 13, 2026`,* and required for all new post-auth experiments starting *`April 27, 2026`*.
Reactions: thank-you-2 (1)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2026-04-03 14:10:14 PDT === 
Message TS: 1775250614.689019
Let's keep the learnings momentum going! :experiment: :rocket: Love seeing the increasing signups for results/learnings and upcoming experiment reviews!
We have 3 great topics for next week.

:blue_siren: <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Agenda> *- Apr 7*
• 11:05 PST [Feedback] Wayfinding:  Global Create Flows <https://docs.google.com/document/d/1zqAvXmQMHVyIE0ZObIkbXnij_mh9sKd70Bf5oFAW80k/edit?tab=t.0#heading=h.4c40og9ra3k3|PRD> <@U0A4STXC88K|Praneethi Komatreddy> 
• 11:20 PST [Results] Support: Intent based routing <@U07NYJQUDS8|Sonia Singhal> <@U05E269C7FH|Dev Parikh> 
• 11:35 PST [Results] Automation: Its just an email <https://docs.google.com/document/d/1VRix9MpOBG0eopQ01l5PH8E624OYgw0Mc_R8er-2RkQ/edit?tab=t.txz7muoubfph|EDD> <@U06QWR7FV9T|Elizabeth Bertasi> 
:point_right: Topic drivers if anything changes, please flag <@U03E6F8KSC9|Aditi Jasani> in thread :thread:. I'll be OOO Tuesday so she'll be running the session. Thanks <@U03E6F8KSC9|Aditi Jasani>! :raised_hands:
Reactions: check-7167 (1)



---

=== Message from Alexandra Pappas (U05A4D12BT8) at 2026-04-08 06:58:10 PDT === 
Message TS: 1775656690.622809
Hi! Friendly reminder that experiment office hours for IXP onboarding are starting today. If you have any questions, please attend.



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2026-04-09 06:00:10 PDT === 
Message TS: 1775739610.781549
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Jenn Reed (U02KEKMTNNA) at 2026-04-13 06:11:01 PDT === 
Message TS: 1776085861.165769
:megaphoner-1707: *IXP is open for Experiments!* 
IXP is now open for all new post-authenticated experiments. *All new post-auth experiments must be on IXP starting April 27, 2026*, so please plan your experiments accordingly.
Feature flags will be enabled on IXP in May.



:movie_camera: *Experimentation Training & Documentation*
If you missed the training or need a refresher:
• Slide deck: <https://docs.google.com/presentation/d/1PCic9d3kUhji1QNDiz6PHZzxIEI_TFU7LfD8A-AmLgk/edit?slide=id.g2a61260a276_0_2#slide=id.g2a61260a276_0_2|IXP Onboarding - Mailchimp Experimentation and Feature Flags>
• Shared drive folder with <https://drive.google.com/drive/folders/1eIXtDipHG1VSyjGeo04bO3y68Xl5QDRi|dowloaded training recordings>
• <https://wiki.cloud.intuit.com/wiki/spaces/MCEXP/pages/3610414315/DRAFT+-+IXP+Documentation+FAQ|IXP Documentation + FAQ for Mailchimp>



:clock1: *Experiment Office Hours*
Have questions or want hands-on help? Join us at office hours!
• Experimentation Office Hours: Wednesdays at 2:30 pm ET  on Zoom (<https://intuit.zoom.us/j/95340390507?pwd=1RrkFUbLFtUPBsUGRbpbp8P6NaNH5c.1&jst=2|Link>, passcode: 323701)



If you have questions or need further assistance, please reach out in <#C03TH2L4QA1|mc-experimentation-support> !
Reactions: rocket (1), thankyou1 (1)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2026-04-13 13:53:10 PDT === 
Message TS: 1776113590.841539
Hi team!  Here's what's on deck for tomorrow.  We still have space on the agenda so grab a slot if you have something to share

:blue_siren: <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Agenda> *- Apr 14*
• [Feedback] x491 Audience & Segmentation  Simplify Choose Method  <https://docs.google.com/document/d/1dg-Z-67zxTIywz0WX2UP7tNSsNttDYVrmNoP0AvMzNs/edit?tab=t.3jt3x81r0s2z#heading=h.mtqdkhcr9ycl|EDD> <@U02KZL81PLH|Caroline Ramirez> 
• [Results] x399 Support: Mailchimp Assistant FAB Scale Test <https://docs.google.com/document/u/0/d/1gASfZnoBrnH2b_HWgbkRDVS1Nzf-Ii_qRusGh3KHJLQ/edit|EDD ><@WH2NN5N3C|Matthew Knell> 




---

=== Message from Experiment Review  (B09BHA86BUJ) at 2026-04-16 06:00:25 PDT === 
Message TS: 1776344425.950309
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Jenn Reed (U02KEKMTNNA) at 2026-04-20 12:11:54 PDT === 
Message TS: 1776712314.715959
:megaphoner-1707: *IXP cutover for experiments is Monday, April 27*
Reminder that *all new post-auth experiments must be on IXP starting April 27, 2026.* If your experiment is currently in the planning or development phase with Optimizely, we strongly recommend launching these on IXP. It should be a relatively low lift to transition an experiment from Optimizely to IXP. If you have questions or need further assistance, please reach out in <#C03TH2L4QA1|mc-experimentation-support> !


:movie_camera: *Experimentation Training & Documentation*
If you missed the training or need a refresher:
• Slide deck: <https://docs.google.com/presentation/d/1PCic9d3kUhji1QNDiz6PHZzxIEI_TFU7LfD8A-AmLgk/edit?slide=id.g2a61260a276_0_2#slide=id.g2a61260a276_0_2|IXP Onboarding - Mailchimp Experimentation and Feature Flags>
• Shared drive folder with <https://drive.google.com/drive/folders/1eIXtDipHG1VSyjGeo04bO3y68Xl5QDRi|dowloaded training recordings>
• <https://wiki.cloud.intuit.com/wiki/spaces/MCEXP/pages/3610414315/DRAFT+-+IXP+Documentation+FAQ|IXP Documentation + FAQ for Mailchimp>


:clock1: *Experiment Office Hours*
Have questions or want hands-on help? Join us at office hours!
• Experimentation Office Hours: Wednesdays at 2:30 pm ET  on Zoom (<https://intuit.zoom.us/j/95340390507?pwd=1RrkFUbLFtUPBsUGRbpbp8P6NaNH5c.1&jst=2|Link>, passcode: 323701)
Reactions: thankyou1 (1)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2026-04-20 14:05:26 PDT === 
Message TS: 1776719126.203379
We have three experiments on the agenda tomorrow sharing out plans and looking for feedback:  two experiments part of *Optimal Setup Program* and one experiment from Support

:blue_siren: <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Agenda> *- Apr 21*
• x472 *OBX* Focused & Payoff-Based Checklist <https://docs.google.com/document/d/1x-bZ6mJp6stN-nLguIIFfl-3EOpD10vj3_Oj-xNiKUo/edit?tab=t.7xhw4pg6heg8#heading=h.gwjnb9ece178|EDD> <@U07RNSH0256|Joshua Fischer> <@U02R9QUKXUL|Shakib Ahmed> 
• x488 *Support* Showing DA and Search Side by Side <https://docs.google.com/document/d/1kLVxQxOCrbRysP4aXuqwBwaRS3jwXF-dHWiKWtjmpN8/edit?usp=sharing|EDD> <@U07NYJQUDS8|Sonia Singhal> <@U05E269C7FH|Dev Parikh> 
• x471 *OBX* Done-For-You-GTKM-Profile (shadow mode) <https://docs.google.com/document/d/1mTh3GLiLl4arfrrLI_hO9FD936CrJbq4UR3vc24LiUk/edit?tab=t.7xhw4pg6heg8|EDD> <@U07RNSH0256|Joshua Fischer> <@U07UCMXJNPP|Jeevisha Anandani> 

Reactions: raised_hands (1)

=== Message at 2026-04-20 12:41:17 PDT === 
Message TS: 1776714077.696449
<@U0AC3JL78DT|Charles Green> has left the channel



---

=== Message from Experiment Review  (B09BHA86BUJ) at 2026-04-23 06:00:05 PDT === 
Message TS: 1776949205.499089
:experiment:  Please sign up <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|here> for an upcoming Tuesday XFN experiment review by *Friday noon EST*
• Three slots avail each week
• Tag the relevant teams or attendees to include in invite



---

=== Message from Jenn Reed (U02KEKMTNNA) at 2026-04-27 07:03:19 PDT === 
Message TS: 1777298599.143209
:check-mark-grn: *IXP cutover for post-auth experiments is now in effect!* 
• All new post-auth experiments must be on IXP moving forward. Optimizely PRs will no longer approved. 
• If you have questions or need further assistance, please reach out in <#C03TH2L4QA1|mc-experimentation-support>. 

:experiment: *Pre-Auth Experiments on IXP*
• Pre-auth experimentation will be available in IXP the week of May 4th. 

:optimizely: *Optimizely ramp down & Global Holdout* 
• All running experiments in Optimizely must be ramped down by *Monday, June 15*. If you have concerns with meeting the June 15th date, please reach out in <#C03TH2L4QA1|mc-experimentation-support>, so that we can review. 
• As part of off boarding from Optimizely, teams will need to make some minor changes to ensure winning variants continue to respect the current Global Holdout. We'll share detailed instructions next week. 
Reactions: ixp-intensified (3), thankyou1 (2)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2026-04-27 13:24:34 PDT === 
Message TS: 1777321474.538889
For tomorrow experiment XFN meeting,  we had two slots cancel.  <@W012EU6L7FG|Payton Camilli> or <@U09FQRBQSRF|Lucas Ruprecht> - do you want those slots? + <@U06QWR7FV9T|Elizabeth Bertasi>.  Please respond :thread: .  TY
cc:  <@U08D0C42PJM|Andrew Spitz> <@U06QRS4SEBC|Rianna Schanno> <@U02KEHAB5U6|Claudia Majors> <@W8FQCFX2R|Pradeep Nagendra>
Thread: 10 replies (latest: 2026-04-28 09:30:28 PDT)



---

=== Message from Phuong Trang (U07TMNHQ20N) at 2026-04-28 08:18:07 PDT === 
Message TS: 1777389487.214269
:blue_siren: <https://docs.google.com/spreadsheets/d/1AF6wo5oxB15BI-l61WcTNwCwdU1zURKyEpxp2XIug6E/edit?gid=152754281#gid=152754281|Agenda> *- Apr 28*
• x499 *Growth -*Intent Aware Onboarding <https://docs.google.com/document/d/1g8fx2QaNeyll92JY59nuEhYUNzO5uZrbvLc_vPTPYKo/edit?usp=sharing|EDD> <@U09FQRBQSRF|Lucas Ruprecht> 
• x371 *Integrations -*Leverage BW to recommend integration <https://docs.google.com/document/d/10hXPz4mjoT1Iva4jvAlUqCNIGaW-F0tym4asMcxUfnA/edit?tab=t.0#heading=h.xpwclgox6ixz|EDD> <@U099JC6013K|Prasad Sawant> 
• xTBD *Automations -*Joins Segment + Personalized recs <@U06QWR7FV9T|Elizabeth Bertasi> 
• xTBD *Campaigns -*Domain Auth <@U0AJVH6EXEK|Amrinder Chawla> 




---

# Thread Replies (selected, where successfully fetched)

The following are full thread replies for the most prominent launches. The Slack thread API returned `thread_not_found` for many other top-level messages, likely because they were broadcast replies surfaced in the channel feed rather than true thread parents.

---

## Thread on: "Joins Segment trigger now live" — Elizabeth Bertasi, 2026-04-28
Parent TS: 1777383920.044159 | 5 replies

- **Andrew Spitz** (2026-04-28 08:40 PDT): woo! very exciting! @Elizabeth Bertasi what does the in product awareness/launch/marketing look like for this
- **Elizabeth Bertasi** (2026-04-28 08:51 PDT): This will be part of the May GTM messaging - cc @Jonathan Rodgers who can speak more about that!
- **Jonathan Rodgers** (2026-04-28 09:01 PDT): @Andrew Spitz - This was included in our April Monthly Updates (product updates for which there is an internal and customer facing version). In addition to that there is a Lifecycle email covering all the feature updates. We also do internal training (Sales/CS) to drive awareness monthly. This won't get a big feature in the May GTM given that this is a Tier 3 launch
- **Andrew Spitz** (2026-04-28 09:07 PDT): got it! I was more-so thinking if there was any light in product nudges to the users leveraging the workaround or that we suspect may have tried to do something like this and given up.
- **Devin Mercier** (2026-04-28 09:22 PDT): THIS IS ACTUALLY HUGE!!! customers have been asking for this for *literal* years! super amazing work team!!!! :rocket::rocket::rocket:

---

## Thread on: "Email OTP Code at Account Activation" — Margarita Caraballo, 2026-04-27
Parent TS: 1777337405.301869 | 2 replies

- **Rianna Schanno** (2026-04-28 06:19 PDT): great impact on top-of-funnel!
- **Danh Dang** (2026-04-28 07:17 PDT): Awesome results.

---

## Thread on: "Annual Plan Self-Serve Experiment" — Jacquelyn Horgan, 2026-04-23
Parent TS: 1776958294.420039 | 17 replies

- **Anish Nahar** (2026-04-23 08:37 PDT): Excited to see what we learn here!! :raised_hands:
- **Navreet Kaur** (2026-04-23 08:40 PDT): Great work team, a lot of hard work went into this. Excited to see results
- **Caroline Kremer** (2026-04-23 08:41 PDT): This is exciting! Can you clarify how this shows up for existing customers (if at all)? How are we attributing churn reduction here?
- **Jacquelyn Horgan** (2026-04-23 08:44 PDT): Existing Paid customers are excluded from this experiment. Existing Free customers <90 days will be bucketed into the experiment at trial start or plan selector. Existing Free customers >90 days will be bucketed into the experiment at load of Plan Selector
- **Jacquelyn Horgan** (2026-04-23 08:47 PDT): All flows can be seen in the Annual Plans Figma. Posting a quick example for Trial Eligible customers here as well [screenshots attached]
- **Lawrence Ma** (2026-04-23 08:51 PDT): Great work all! Thanks to our cross team partners and everyone involved to getting this out!
- **Ethan Ham** (2026-04-23 09:13 PDT): @Caroline Kremer we'll be estimating churn impact through a combination of leading indicators like Annual Plan take rate and onboarding activity trends for Annual Plan users (who is taking AP), and will also track churn actuals against control as the data ages for new bookings to see if things are trending as expected. There are a lot of variables at play with this experiment, but happy to connect on the details!
- **Diana Williams** (2026-04-23 10:21 PDT): Great! Please keep us updated on forecast to actual for this launch!
- **Ashley Goodson** (2026-04-24 07:13 PDT): Hey team, if inbound sales reps have a customer less than 10k contacts requesting an annual plan, will they have the option to offer it if it's not showing up on their end (control group)?
- **Amanda Hunt** (2026-04-24 08:03 PDT): Pinging @Jacquelyn Horgan for confirmation and additional context, but yes. The seller should use the Sales Offer tool to offer annual plans - @Jacquelyn Horgan can you confirm the discount strategy in this use-case?
- **Rhomaro Tesfai-Powell** (2026-04-24 12:55 PDT): @Ashley Goodson Yes, the sales rep will be able to the Sales Offer tool to honor the Annual plan offer for a customer in the control. However, if the customer is on a trial then their trail will end immediately once they have purchased the annual plan.
- **Ashley Goodson** (2026-04-24 13:02 PDT): Great to hear. We have had customer below 10k contacts asking for an annual option for the last year and a half!
- **Ashley Goodson** (2026-04-28 10:17 PDT): @Rhomaro Tesfai-Powell We are not seeing the option to offer the annual plan for tiers below 10k on the sales offer tool. [screenshot]
- **Rhomaro Tesfai-Powell** (2026-04-28 10:27 PDT): Thanks for flagging. I will report this to the team.
- **Rhomaro Tesfai-Powell** (2026-04-28 10:30 PDT): @Ashley Goodson Are you currently working with a customer? I want to ensure we are not slowing down a deal while we are addressing the issue.
- **Jacquelyn Horgan** (2026-04-28 12:43 PDT): **Sales Update:** Releasing AP in the Sales Offer tool for Essentials and Standard < 10K was not part of the scope of this release. Additional conversations would need to occur across all stakeholders to release those plans/tiers to managed channels. For the duration of the AP Experiment - If you have a customer who is in the variant, you'll want to direct them to purchase within the app. There is no impact to customer here - only short term impact to Sales Offers during the duration of the experiment. Once we have a statistical read on AP experiment performance, we will share next steps with all teams. CC: @Ashley Goodson @Rhomaro Tesfai-Powell
- **Ashley Goodson** (2026-04-28 13:20 PDT): Oh, okay. Thank you

---

## Thread on: "Place of Supply-Based Taxation" — Jacquelyn Horgan, 2026-04-22
Parent TS: 1776862994.666289 | 4 replies

- **Zia Uddin** (2026-04-22 06:10 PDT): Amazing job, well done to the whole team on a significant compliance milestone
- **Rhomaro Tesfai-Powell** (2026-04-22 06:43 PDT): Great work, team!!
- **Yilmaz Kara** (2026-04-22 07:33 PDT): Thanks team. Great job!
- **Anish Nahar** (2026-04-22 08:41 PDT): Congrats on the launch! Great job, team!

---

## Thread on: "Meta Custom Audience Integration: GA" — Srilekha Chandrashekar, 2026-04-21
Parent TS: 1776776408.288969 | 3 replies

- **Diana Williams** (2026-04-21 18:17 PDT): Great job such an important integration and feature for our customers
- **Jamal Simpson** (2026-04-27 06:19 PDT): Hello! Is there a team/contact we can connect with if we have questions on the integration or need assistance with troubleshooting?
- **Abby Barnett** (2026-04-27 06:25 PDT): Hi @Jamal Simpson - you can use this channel for questions! #idi-coins-core-integrations-support

---

## Thread on: "The Watchtower (SMS regulation AI monitor)" — Connor Callahan, 2026-04-20
Parent TS: 1776711908.028079 | 4 replies

- **Emily May Curtin** (2026-04-20 12:40 PDT): This is awesome! If you ever find yourself needing a more robust backend or auto refresh, come visit us in #mc-business-enablement and let's talk!
- **Christy Sullivan Filitor** (2026-04-20 12:58 PDT): Would love to connect on the Next Steps area as we have some shared interests and I'm always looking for new monitoring strategies
- **Connor Callahan** (2026-04-21 10:04 PDT): @Emily May Curtin - Just passed the test. Will definately keep you all in mind. @Christy Sullivan Filitor - Would love to connect. Will reach out to setup some time! We have gotten a lot of value out of the #mc-competitive-intelligence channel so still plan to be a happy customer
- **Adam Anger** (2026-04-22 05:51 PDT): this is so great -- nice job to the team behind this!

---

## Thread on: "x290 Inline Contact Search in Audience" — Payton Camilli, 2026-04-14
Parent TS: 1776205376.985479 | 7 replies

- **Payton Camilli** (2026-04-15 11:41 PDT): Seeing some positive feedback! [link]
- **Jessica Lin** (2026-04-15 14:09 PDT): Adding @Ryan OConnell from CDP team!
- **Nathan Snell** (2026-04-15 15:35 PDT): @Diana Williams nice customer feedback already!
- **Diana Williams** (2026-04-15 16:58 PDT): Yes!!!
- **Payton Camilli** (2026-04-16 07:58 PDT): Another :smiling_face_with_3_hearts: [image]
- **Navjot Cheema** (2026-04-16 13:05 PDT): :excite:
- **Payton Camilli** (2026-04-27 14:26 PDT): [final results readout] x290 Experiment Landed: Inline Contact Search in Audience. DEMO video. Apr 13 → Apr 23, 2026 (11 Days). Primary: Campaign Creation Rate (within 7-day post-search): +2.91% lift = Big, Clear Winner. Secondary: Email Create Rate +0.06% (Flat); Avg. Email Creates per C1 -1.71%. Guardrail: Payoff Complete Rate +0.31% lift (significant) — No harm.

---

## Thread on: "Nuni Sections Manager — Launched and Landed" — Ose Amiegheme, 2026-03-31
Parent TS: 1774972805.695499 | 5 replies

- **Bethany McDaniel** (2026-03-31 10:46 PDT): This is SO EXCITING and something users have been asking for FOR YEARS! Seeing users' initial reactions to this in real time was such a treat. Here's a quick (3 minutes) video with some of those initial reactions and at the end, users explaining the benefit they immediately see by having this ability. Incredible work team!!!!!!
- **Alex Wilson [email oncall]** (2026-03-31 10:52 PDT): Users have been asking for this for *years*—even before I joined 12 years ago. Really proud of this team. The level of thought and intention that went into this work truly shows, and our users are already feeling the impact. This goes well beyond anything we offered in Nea! This is something entirely new for email editing at Mailchimp. And we're already hearing it called a game changer. Amazing work, team!!
- **Michael Hawkins** (2026-03-31 10:54 PDT): Super proud of the collaboration and process behind building this feature - y'all are awesome!
- **Diana Williams** (2026-03-31 11:05 PDT): Yes!!! Love it!
- **Erin McCue** (2026-04-01 09:27 PDT): Really really excited about this. The team very intelligently broke this down into 3 phases that provided clear customer value at each one, allowing them to work longer-term towards our end goal: saved sections. (Coming soon!) Especially great cross-functional partnership on this project. Huge thanks for the teamwork here!

---

## Thread on: "WhatsApp Private Beta LAUNCHED" — Devin Mercier, 2026-03-20
Parent TS: 1774026751.825339 | 14 replies

- **Rujuta Apte** (2026-03-20 10:14 PDT): HUGE congratulations to the whole team! This has been in the works for years and we finally did it!! So proud!
- **Alina Rainsford** (2026-03-20 10:15 PDT): What an amazing milestone for our Messaging offering! Congrats everyone, so excited for our learnings!
- **Eric Anderson** (2026-03-20 10:15 PDT): yay! go team!!
- **Satish Sambandham** (2026-03-20 10:17 PDT): Congrats team, so many attempts over the years, excited to see this finally launched!
- **Matt Idema** (2026-03-20 10:21 PDT): Very excited about this one!
- **Vivian Wang** (2026-03-20 10:37 PDT): Go team!!! Killing it
- **Payton Camilli** (2026-03-20 10:55 PDT): Can't wait for the learnings!! Way to go everyone!
- **Diane Hahn** (2026-03-20 11:06 PDT): So stoked to get this in more customers' hands + continue evolving for our customer needs!!
- **Diana Williams** (2026-03-20 11:08 PDT): So excited for this effort to scale but excited for the learnings in the near term too!
- **Neil Desai** (2026-03-20 12:06 PDT): BIG DEAL!! It is not every day that you get to announce a *new channel launch*!! Congratulations!
- **Ruth Libowsky** (2026-03-20 12:27 PDT): 3 years after starting this journey ... we did it!!
- **Marco Traini** (2026-03-24 11:57 PDT): Congrats team!
- **Matt Idema** (2026-03-24 11:58 PDT): Might be my favorite launch of the entire year :green_heart:
- **Andrew Firstenberger** (2026-03-25 09:37 PDT): This is great! Congrats all and thank you for all the hard work.

---

## Thread on: "Recommend SMS to C1s with C2 Phone Numbers in Audience (x287)" — Connor Callahan, 2026-03-20
Parent TS: 1774008120.314429 | 5 replies

- **Neil Desai** (2026-03-20 07:11 PDT): HUGE WIN! And an incredible use of the propensity model findings. Great work team!
- **Rujuta Apte** (2026-03-20 07:19 PDT): Such a great example of data guiding design and product decisions and resulting in massive impact
- **Andrew Spitz** (2026-03-20 08:14 PDT): so awesome! Great job team!
- **Connor Callahan** (2026-03-20 09:32 PDT): The experience curtesy of @Ashley Lawrence! [animated gif]
- **Diana Williams** (2026-03-20 11:03 PDT): Love those stats!!! Well done!

---

## Thread on: "Analytics Agent V1 (Project Alfred) test update" — 2026-03-13
Parent TS: 1772468019.988369 | 1 reply (concise)

- Analytics Agent V1 launched as A/B test to 50K user cohort. Lift on primary metric and key downstream metrics: +6% to email campaigns sent per user (2.69 → 2.86, >99% prob to beat control); +0.7% to % of users sending 1+ email campaigns (70.1% → 70.6%); positive trending in active churn reduction and % of MC attributed revenue. Adoption: 85% engagement when users viewed analytics agent; 3000+ insights generated to date. Customer voice: "The AI gives me a depth of intelligence and analytics that is eye opening...", "The responses were in depth and synthesized the data for me clearly." Custom analytics use case: applied to a churn-risk user (1300 MRR) with custom reporting request — solved instantly vs weeks. Next: scale to larger group in 2 weeks for v2 (beta).
- **Diana Williams**: Excited to get this feature in the hands of our users. Please make sure we have an easy feedback mechanism for feedback and quality issues.
- **Stephen Yu**: Thank you! Yes, we monitor user responses regularly and have feedback mechanism in place for users to submit feedback.

---

**Note on coverage gap:** There are ~95 additional top-level messages in `#mailchimp-launched` and ~25 in `#mc-experimentation-xfn` that have thread metadata but the Slack thread API returned `thread_not_found` for most when queried — this typically happens when a top-level message in the feed is itself a broadcast of a thread reply (the `thread_ts` differs from `message_ts`), or the parent has been deleted. The full top-level messages including all metrics, links, team credits, and reactions are captured in the main transcript file. If specific thread content is needed, those can be retrieved on a per-message basis.
