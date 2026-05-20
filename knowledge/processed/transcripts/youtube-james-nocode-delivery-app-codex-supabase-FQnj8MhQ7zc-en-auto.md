# Build a REAL Delivery App with Codex and Supabase (Full Tutorial)

## Source Metadata

- source_url: https://www.youtube.com/watch?v=FQnj8MhQ7zc
- video_id: FQnj8MhQ7zc
- channel: James NoCode
- language: en
- is_auto_generated: True
- retrieved_at: 2026-05-20T16:40:48Z
- source_type: youtube_video
- confidence: verified source capture; auto-caption accuracy not independently verified
- raw_artifact: ../../raw/youtube/youtube-transcript-james-nocode-build-a-real-delivery-app-with-codex-and-supabase-full-tutorial-FQnj8MhQ7zc-en.json
- extraction_strategy: yt-dlp
- warnings: timedtext_empty_used_ytdlp_fallback

## Normalization Notes

- The raw JSON preserves the extractor output, including original caption segments and `plain_text`.
- This Markdown transcript collapses repeated rolling auto-caption fragments by keeping only incremental text already present in consecutive captions.
- No missing words were inferred or reconstructed beyond de-duplicating overlapping caption windows.

## Transcript

### 00:02

In today's video, we'll be building a complete delivery style app. Think of something like Uber Eats or Global.
Throughout the process, we'll be using an array of proven tools to help us. The end result will be a real mobile app
that we can use and distribute. Now, before we get started, let's quickly talk about the tools we'll be using throughout
this build. The first tool and our main tool is Codeex, which will be our AI agent of choice. I've been using Codeex for
a while now and have written nearly a million lines of code building all kinds of apps. The next tool that we're going
to be using will be Google Stitch. This will be our designer tool of choice which we'll use to generate beautiful
mockups and designs for our app. And last but definitely not least, we'll be using Superbase, which pretty much needs no
introduction. It is a state-of-the-art proven Postgress SQLbased backend that is used by millions of apps and is a super
solid choice for this app. I've been using Superbase to build all kinds

### 01:03

of apps and it is going to be absolutely perfect for this specific app. And we'll also be using various open-source
tooling to help us build out this entire app as we go along. Now, before we write even a single line of code, we want to
ensure that we have properly decided the kind of stack that we're going to be using to build this app. A lot of app
builds go wrong because the tools are chosen too quickly. So, we are going to ask Codeex to compare the realistic
options first. For this project, we want a real mobile app that can run locally in the iOS simulator, but we do not want
native iOS complexity. Now here I'm inside of Codex and before we can start building our app, we need to first create a
project. And so I'm going to click here and I'm going to start a project from scratch. And I'm just going to call it
delivery app. Click save. And now we have this project defined here. And here we can create new chats that are going to
be assigned to this project only. And that

### 02:05

way they'll get the context of the entire app including the files that we're going to write all the environment stuff
and they'll be able to easily figure out what to do. And the next thing that we want to do is we want to start a new
conversation so that we can start building the app. Now the first thing that I want to do is I want to ask codeex for
some stack suggestions. Okay. So the prompt that I'm going to be using will be something like this. I want to build a
complete customerf facing delivery mobile app tutorial. So help me choose the best stack before we start coding. Now
here I typically choose full access. I've realized that that works really really well for me. And here you can select a
model. I typically stay on the latest model which is at the time of recording this video is GPT 5.5. And I typically
keep it to high for intelligence unless I have another reason to select another mode. Now another important thing that
you want to do is you want to make sure that you use plan mode. So you if you click over here, you can select this
toggle to

### 03:05

enable plan mode. But a much easier way would be pressing shift tab. Okay. So we're going to go ahead and execute this
prompt. And let's see what it tells us. All right. And this is what we got back. It says here I choose Expo, React
Native, Typescript, and Superbase. So your current preference is the right one for this tutorial because it best matches
the goal. A real mobile app that can run in the iOS simulator, uses native mobile patterns, stays beginner friendly, and
still has a clean path toward production. Okay, so this is the recommended stack, the app, the routing, the backend,
local state, data access, and the runtime. Now, with a quick glance on this comparison table, you can see some different
stacks and at the level to which they fit for what we were trying to do. So here we have React Nex.js JS which is a web
app and the fit here is medium and so this is fast to build easy superbase integration but it

### 04:07

teaches a web PWA delivery app okay not a true mobile app and this is absolutely true because we won't really be
building a true mobile app okay here we have flutterflow no code also the fit is medium good for quick visual building
and supervised wiring but weaker for a codeex centered coding debugging tutorial and I know from experience that you can
definitely build an app using flatterflow. But in this video, I obviously want to build something using real code using
a real AI agentic workflow. If you look at this last row, we have expo react native and this is the highest fit native
mobile feel, fast iteration, iOS simulator support, TypeScript, strong superbase compatibility, and less setup burden
than raw react native. And this stack here is actually used by pretty much everybody who wants a really kind of
nononsense, no fuss stack without dealing with all the primitives and all the little

### 05:08

details and stuff like that. And so from where I'm standing, this is the best approach if you want to build a real
native mobile app. And here it tells us why Expo wins here. Expo gives us the teaching sweet spot. React Native's own
docs say most new React Native apps benefit from using a framework such as Expo because it provides routing libraries
and production ready tooling without making you manage native files immediately. And this is a great great approach.
Okay. So now that the stack is clear, I'd like to have a visual architecture or a visual depiction of the app before I
go forward and start building it. This will depict the screen flow and the data model and so we can see if they line up
correctly so that every screen has a clear reason to exist. Create the visual architecture and entity architecture for a
beginnerfriendly expo food delivery mobile app tutorial. Include all of this supporting systems minimum version one

### 06:11

entities guard rails. Right? Exclude all of this. We don't need any of that. And I also want to preface that it uses
this image gen. We're still in plan mode. We're going to go ahead and run that. Here, we want to create two
instructional raster visuals with the built-in image and workflow. We have the visual architecture and the entity
architecture. So, we want to show the customer app flow as connected screen nodes. Very very important. And for the
entity architecture, we want to show the different entities, right? So like you know users, profiles, cards, cart item,
restaurant, menu item, all of that stuff that will be used throughout the build process. Here we have the test plan. So
I'm going to go ahead and submit this. And we should see some mockups showing us the visual architecture as well as the
entity architecture. All right. So it went ahead and created these two mockups. Okay. So this is our visual architecture
and as you can see it includes the codeex workflow, the Google

### 07:12

stitch handoff, the expo react native app with the different things and then we have the customer app screen flow. So
this is the main screen flow. I typically do not include this. It's just in this tutorial I wanted to show you the
different aspects of the app. And if we click here we can see that here we have the expo react native food delivery app.
This is the entity architecture. Okay. And these are the various entities that are going to be representing the various
concepts in the app. Right? So user profile, you know, a restaurant, a menu item, a menu modifier, a cart, a cart item,
a order order item, order status event, all the different things as well as their relationships. So as you can see,
there's a bunch of lines, a bunch of arrows that are used to represent the different relationships. And as you can see
one and n that means a one to many relationship right because a restaurant can have multiple menu items okay in their
menu essentially and

### 08:14

a menu item might have a menu modifier and as well as you know a user might have multiple locations a card can have
multiple card items stuff like that and there's also some inter relationships as well so like a a restaurant can have
multiple menu items but A menu item is also linked to a cart item, right? Because you can have one menu item depicted as
multiple cart items here. And here we have the different orders as well. And it did a really good job because not only
is it displaying all the different entities, but it also grouped them together with different colors. So we have light
blue, kind of light greenish, we also have this reddish. And so after looking at these two diagrams, I immediately have
a much better understanding of what kind of app that we're building, especially this diagram right here. I want to see
the flow. I want to see the scope of the app. I want to understand number one,

### 09:17

what is being built in this app, version one. And most importantly, even more important is what is not being built.
Right? So, as you can see, excluded from version one. We have a bunch of things like messaging, maybe a bunch of other
things, but I want to see what's actually included, right? So, browsing restaurants, search filter, restaurant detail,
menu items, all of this. And this is super super important because what a lot of people do is they just want to cram as
many features as possible into that first version. And that's definitely not what you want to do, especially when you're
using AI agentic coding, right? You want to start basic. You want to you want to start in steps. Now, at this point, we
have a general understanding of what kind of app that we want to build. We have the right stack. We also have the data
model. And so, what we need now is for Codex to inspect the actual project and turn that

### 10:17

into a phased implementation plan. Right? So the key is to avoid building the whole app in one giant pass. We're going
to be defining the smallest useful vertical slice. Decide how each face will be used. Decide how each face will be
tested and see if there are any possible issues before they turn into debugging problems. So what we want to do is we
want to inspect this project and propose a beginnerfriendly implementation plan for a complete expo react native
delivery app. The app should include restaurant browsing, search, all of these things. We want to use Superbase for O
database RS and persistence and we'll set it up later. And we want to be using iOS simulator as the main verification
target. Okay, so at this point we do not want to edit anything. Okay, so I'm going to go ahead and jump into plan mode.
So it came back with this plan, beginnerfriendly expo delivery app

### 11:18

implementation plan. This is the current project structure. It is empty and it it is also not tracked by git. And this
is another thing that we definitely need to make sure that we're going to be using. There are no app files, nothing. So
the likely entry points after scaffolding is going to be this. We're going to be using expo router because expose
current scaffold supports filebased routing with TypeScript and Expo documents iOS simulator workflows directly. And
this is our existing stack that we already decided on earlier. And so here we have the safest implementation phases
scaffold plus simulator baseline superbase o all of this. And so now what we need is a real mobile project. We need
something that just works so that we can ensure that everything that we built on top of it is going to work. And so
we're going to be scaffolding a clean expo project with TypeScript and an Expo router. So the app has a simple

### 12:19

foundation, right? This part is not flashy. It's not anything special, but it matters. It matters a lot. Once the
project structure and start commands are known, every subsequent feature has somewhere stable to go. Set up the Expo
React Native project for the delivery app. Okay. inspect the current folder first. If there's no suitable export expo
project scaffold one with typescript and export router and I'm also going to add a step so that it creates a git repo
and I've added this at the bottom here. Okay. And so we're going to go ahead stay in plan mode but this time we are
going to execute it. All right. So here's the plan and quickly scanning the summary. The folder is empty and it's not a
git repository. There's no suitable export project yet and that's fine. I'm going to scroll down and I am quickly
scanning the acceptance criteria. Project contains all of this and I want to make sure that we do not do any future
steps here. No

### 13:21

superbase, nothing of that sort. I want to ensure that it doesn't create do not add superbase. Perfect. Because that is
something that we're going to do later. And so this looks good. Let's go ahead and implement this. All right. So it has
finished and it says here implemented the expo scaffold and initial check-in created a fresh expo React Native
TypeScript app using the official export router tabs template here. Main entry points are here. Now it does say that the
iOS simulator is available and the expo go was installed on iPhone 17 but core simulator timed out. Okay. And it's
actually running the the simulator right here. And so if we click over here and it's not clear if the app is loading.
And so this is something that happens all the time. And so what we're going to do is we're going to exit the simulator
and we're going to tell it to start it again. Go ahead and restart the simulator and run the scaffold app. And

### 14:23

let's see if it's able to do it. All right. So now it's looking at the screenshot of the simulator and is trying to
figure out if the app has been installed, if it's running properly. And this is an important step because if we can get
this working, then nothing is going to work from this point on, right? Any of the future steps are pretty much
pointless. So it still had some issues with launching that app. And so it's telling us the issue looks specific to core
simulator app launching on this booted iPhone 17 runtime. And so it's going to try a different fresh simulator device.
And now it's telling us that a second fresh simulator device shows the same time out after installing Expo Go. And as
you can see, if we click here, actually that works. That now works on the fresh device. So let's see if it's able to see
this. So I'm going to stop it right here and I'm going to tell it

### 15:24

that the app does load. Okay. So, it acknowledged what I told it and it says that you know since Expo go itself opens
fine we'll avoid another path and we'll do something different and that is important because you know throughout
development you're going to be experiencing these little you know quirks these little road bumps if you will and you
kind of have to take over the controls every now and then do something tell it that it worked and then it's going to
internalize that and continue. So in our simulator we can click on expo go and we have this deployment server and this
is the exact same thing. Local host is this 127001. It's the same thing. And so if we click over here we should be able
to see everything but we do get another error here. It says here could not connect to development server. So let me go
ahead and check what this all about. Going to copy that and I'm going to go ahead and paste it. So that red screen means
expo go open the server open the project URL but Metro is not reachable from the

### 16:25

simulator at this host port. I'm checking whether the dev server is still alive. Let's see. And this is a minor issue.
This is not a serious issue. This is mostly a a kind of a networking issue that will be fixed relatively easily. And so
now when we start this and we click on our delivery app, it opens the project now. There's no issues, there are no
errors, nothing of that sort. And we have even two tabs. We have tab one and tab two. So at this point, we know that as
we continue building, we are not going to be dealing with those stack issues, infrastructure issues because this is our
smoke test. And you definitely want to make sure that you get this done early on, right? Not later because later you may
have other issues. And and so now that the blank scaffold app runs, we can continue by building our UI

### 17:26

mockups. Okay. Codeex can turn our app scope, screen map, entity model, and mobile constraints into a precise prompt for
Google Stitch. And this gives Stitch the right context before we start generating screens. The prompt needs to describe
the full customer journey, the key app states, the visual direction, and the boundaries and everything that's included
in the first version of the app. Here's our prompt to create another prompt to create a prompt for Google Stitch because
we want Codeex to create this prompt. We don't want to go to Google Stitch and start typing a prompt from memory or
worse type something very very simple. Create a Google Stitch ready prompt for a customerf facing food delivery mobile
app. Okay. Use this product scope etc etc. So I'm going to jump into our plan mode in case it wants to ask me something
and I'm going to send this. All right. Now take a look at

### 18:27

this prompt here. This is a monster of a prompt. Look how long it is. Design a polished customer-f facing food delivery
mobile app for iPhone. Now take a look at this prompt. It has five parts. Visual style component direction guard rails.
This do not design a driver app output. And then we have a variation checklist. Okay. Does it clearly cover browse? Does
it feel like this is for us? And so we're going to go ahead and copy this. And now we're going to jump into Google
Stitch and we are going to design the actual UI UX screens here. So here I am with Google Stitch loaded here. And this
is our main screen. And if you've never used Google Stitch before, I actually have a video that you're going to see
right there. But essentially, this is AI system essentially that generates UI, UX, screens, mockups, stuff like that.
And

### 19:27

there's various ways that you can use it. You can create your own prompt and enter it here, but I would not recommend
it. You want to create a very, very specific prompt that tells Google Stitch what kind of stuff you want to see, how you
want to see it, and what kind of stuff you don't want to see. You want to have guard rails, constraints, very, very
specific, very, very important. So, we're going to paste this prompt right here. We have here an app selected. We can
also include upload files, website URL. We can enhance the prompt. We don't really need to enhance this prompt because
this is a prompt that we did not generate. This is something that our system generated. So you don't want to modify this
prompt. This is a solid prompt right here. Now here you can also select some presets. And here we have the model. So
three flash, thinking, redesign or ideate. Okay. Now you want to start with three flash. You can also use thinking. I'm
fine with just three

### 20:28

flash. And we're going to go ahead and execute this and see what it comes up with. So, this is the color scheme that it
chose for our mockups that it's going to be using. So, it looks fine to me. All right. So, it's still generating the
screens here, but one of them has been generated. And this is our menu kind of screen where we can take a look at the
actual dish. And it looks pretty good. Classic cheeseburger, the price, you can choose what kind of cheeseburger. And
now we can see the rest of the screens. And as you can see, they all follow this color scheme. This kind of reddish
black. These colors here are grayish. These are this is the outline. These are the buttons, the labels. This is the
search how it's going to look. The text input, you know, as far as I'm concerned, it looks pretty decent. We have here a
status screen, order

### 21:28

confirm, delivery status, the main screen with deliver to. So, this is the final list of screens. We have the home
browse, restaurant detail, the checkout, customize item, and the order tracking. And this is a nice start for our app.
The initial kind of required screens that the app needs to have before we add more and more screens as we add more and
more features. Now, Stitch has lots and lots of features. You can do a lot of things. So for instance you can select
this you can click here you can do an instant prototype you can do variations you can regenerate heat map modify all
kinds of things but I am fairly happy right to my untrained eyes it looks fairly good and so at this point what I want
to do is I want to get Codex to import the designs or have Stitch export the designs into

### 22:31

codecs. Okay. And how do you do that? Well, you simply click on export here and you can select you want to select all
your screens first. Command A. And now you can export it via several ways. AI studio Figma MCP as a zip copy to
clipboard project brief or create a stitch react app. Now we want to select MCP here. The first time you do it, you will
have to set up MCP. So, if you click here, it's going to tell you how to set up MCP. You want to select your client.
We're going to select codeex. And now, it gives you instructions. But most importantly, you get this API key. Now, my
codeex is already set up, right? So, if I press command, comma, and I go into MCP servers here, I already have Stitch
somewhere right here. And so, it's not enabled, which is fine. But even if you do not have it set up, you can simply go
back and you can sell

### 23:31

codeex to set it up. Really easy. Go back to Stitch. And what you can do is you can simply copy this, paste this, and
say, "Hey, set up this MCP server." So the first time you do it, it's going to set it up. But for me, it should tell me,
"Hey, you already have it." And so it's going to check if the key is set up, everything is set up correctly. So let's do
this. And this is by far the easiest way to configure MCP servers. And so it's telling me that the Stitch MCP server is
already present, but it is currently disabled. So we're going to go ahead and enable it. And it enabled the existing
Stitch MCP server here. So if we press command, comma again, go into MCP servers, we have it here. It's still disabled.
And that is because, well, now it's enabled. So you may want to do that just in case. And so once we have that done, the
next thing that we need to do is we need to get codeex to import all of our designs from Stitch. And

### 24:32

thankfully Stitch is able to provide us with really good instructions to do that. And here we were in setup MCP section.
What you want to do is you want to exit out and you want to click on copy prompt. You're going to copy this prompt and
you're going to go back into codeex and you're going to paste it. So you have these stitch instructions. Get the images
and code for the following stitch project screen. Okay, this is the project and all of these screens. So I'm going to
jump into plan mode. I'm going to run this. And in fact, this is a type of prompt that you don't really need to do it in
plan mode, but just out of habit, I typically like to jump into plan mode in case it wants to ask me something, confirm
something, and even if there's nothing it needs to ask, it doesn't waste a lot of time. It just gives me that extra
peace of mind. Okay. And so here's the plan. We're going to be downloading the Stitch assets. Now, before I hit submit,
I want to add

### 25:33

another prompt that will do something useful with those assets. So, I'm going to press escape. I'm not going to run
that. And I'm going to use the following prompt to grab those assets. Okay. So, inspect this export delivery app project
and the Google stitch handoff artifacts before editing files. Stitch handoff may include all of these tasks. Identify
where these design artifacts should live in the project setup or document guard rails. Do not edit the app files yet. Do
not add superbase. And this should properly import the designs that we have in stitch and merge them into what we have
in our own app. So I'm going to go ahead and run this. Now it knows about the stitch stuff because that was the previous
prompt. And so when we combine both of these prompts, it will actually do something useful with the stitch artifacts
with the stitch markups. So design artifacts have a clear home under stitch before they're used for

### 26:34

implementation. The MCP connection is documented. Implementation guidance, design artifact plan, everything. So let's go
ahead and run this prompt. So it has finished working has implemented the stitch handoff plus the first mock data expo
delivery UI slice. So the first UI UI uh piece. So it added these uh stitch handoff source files replaced the starter
expo tabs added my customer flow screens. So this is the moment of truth. Let's go ahead and see how this looks. We're
going to go ahead and run this app here. And right here there's no app. No apps are running. So we need to start our
server. So let's go ahead and start the expo server. And now as you can see the app is running in this development
server. So we're going to go ahead and open this project. And this is our app. Okay, this is the front page. We have the
browse screen. We have

### 27:35

different things we can select. We can scroll top rated. And nothing is working just yet. We can change the address, you
know, we can search. It's just the mockups. Looks really good. We have the order screen here preparing. Let's go into
browse. And let's go ahead and compare this to the mockups that we initially generated in Stitch. So, here we are in
Stitch. And the goal was to create very close mockups. And they look really close to me. They look good enough. I mean,
they look like I don't know 90%. This this they look 95%. They look very similar. I mean, yeah, this thing here has
icons, and we can fix that later. Popular. Now, we don't have recently viewed nearby restaurants. We don't have this
view cart. Well, we're going to see that later when we can. We have that flow. Harvestable add to cart.

### 28:35

Oh, yeah. We do have it. Look at this. Except it's $1,7.99. It should be $1450. Okay. So that is just random data, you
know. If I add this again, two items, but it's it should be$,450. So So it should be like what? 29 bucks. And for some
reason, it shows 32. Okay, we'll fix that later. Let's add this. Okay, I'll click here. And it doesn't list the price
here. We can remove that. Yeah, it works. Ah, because of the delivery fee and the service fee. That's why that's why the
price is different. So if we add 1450. Yeah, because of all the fees. So if we click here, $1.99 150. So it even has
that. I mean it looks pretty good. And this is mock menu data now. Superbase back catalog comes later. And so what I
want to do now is I wanted to finish all the pages. Insert all the available mockups cuz right now we only have two. And
if we jump into sketch, we have browse, order, profile.

### 29:35

And so we want to make sure that it includes all the mockups. Go ahead and include all the mockups. Just a simple
instruction here because we already had a more complex prompt earlier. So it should know exactly what to do. So when you
say the app should display all stitch mockups, which which direction do you want for this pass? Not a mockup gallery,
but we want to replace app screens. We want to rebuild UI to match. That's what we want. The five stitch mockups as real
expo React Native screens, not as screenshot samples. That's exactly what we want. All right. So, it has finished and it
has implemented the stitch matched React Native UI pass. Okay. So, it has updated all of this. And so, now if we open
our simulator and click here, we should hopefully have this app running. So, we can click here. That's going to go ahead
and load the project. Here's what we see. Now, this says home now. And we

### 30:36

still don't see all the tabs, right? Because if we go back to our stitch, we have browse order profile. Okay, we have
stuff on the bottom. Go ahead and copy that. On the main page, the navbar should include the following tabs. Linking to
other screens. Our app only has home and orders. Ensure it shows all the tabs and they link to their respective screens.
Let's go ahead and run that. So here it needs to update the tab bar. So it shouldn't take that long. It should be a
quick change. All right. Implemented the four tab stitch style bottom nav. Let's go ahead and see. And there it is.
Browse orders profile. Look at that. Looks really nice. All right. So, now that we have our app working, the next step
is to connect our back end. And our back end is going to

### 31:37

be Superbase, which is a super proven backend that's used by thousands and hundreds of thousands and even millions of
apps worldwide. Now, we're not going to be setting up Superbase completely. We're going to get Codeex to do it for us.
But there's still a couple of things that we need to do in our Superbase dashboard. So, here I am in my Superbase
dashboard here. And as you can see, I have a bunch of projects here that represent the different apps that I have
created over time. And so, what we need to do is we need to create a new project here. And we're just going to call this
project delivery app. Codex delivery app. Just going to have a password here. Generate something. Doesn't really matter.
and we're going to go ahead and create this project. So, this project is being created right now as you can see. Now,
we're not done yet because we want Codeex to set up our whole Superbase and configure everything without us needing to
do pretty much anything. And for that, we need to go into account settings, account

### 32:38

preferences, and we need to click on access tokens, and we need to create a new token. So, I'm going to go ahead and
label it Codex delivery app. generate this token. And now we have this token generated. I'm going to go ahead and copy
it. Next, I'm going to ask Codex, what kind of configuration do I need to configure our MCP server for that newly
created project. This depends on the different MCP setups. Some require these values, other require these parameters.
And so I need to know what they need. I know that it's probably going to require our project ID as well as the access
token. And so let's wait for codeex to look it up and tell us exactly what we need for the official Superbase MCP
server. You mainly need the MCP server URL. We have that the project ref. That is what we need to provide the access
mode, not

### 33:39

read only feature groups. We're going to skip all that authentication superbase access token. And that's pretty much it.
And so I'm going to give it our access token. Access token is this. And I'm going to go ahead and fetch the project ID.
And in fact, you can just copy this whole thing. This project URL here. Copy that whole thing. And it's going to figure
all of this out. I'm going to paste that. And I'm just going to say project URL here. Config the MCP server. Again, you
never really want to paste sensitive tokens or keys in your chat. This is not good practice, but we're making a demo app
and I'm going to be disabling this access token shortly and that's why I'm okay doing it. So, now we've configured the
Superbase MCP server in my local codeex config. This is the current setup enabled is true. Everything is fine. And if
even if we press command comma and go into MCP servers and select this, you can see

### 34:40

that this is fully configured. We have the token here and we have the project ID here. So now I'm 100% sure that it
works. But it's always a good idea to test to make sure it's able to connect and we are connecting to the right project.
And so what I'm going to do is I'm going to say using the Superbase MCP server list our tables. And if we go to our
Superbase dashboard here and we go into our table editor, you can see that we don't have any tables, right? This this is
a brand new Superbase project. And so that's what we want Codex to tell us. We don't want Codex to tell us, hey, I can't
access your database or list a bunch of tables. And it says here I can't list the tables from superbase was added but
the MC are not loaded in this session. Okay. So let's go back here. MCP server. Let's enable disable and do a restart.
And let's see if that works. Now it's no longer giving us an error

### 35:42

message. It says that Superbase MCP is connected. Current public schema tables none. And that is exactly what you want
to see. You want to make sure that we are connected before we start, you know, creating a super complex schema because
what you don't want to happen is configure some other project, maybe a previous project that you used for another app
and then pile all this new schema in that old project and create a big mess. Okay, so now we know that everything works
and we are ready to continue to the next step. So now that Codex has the superbase project detail it needs, we can
define the back end properly. This is where the app gets real tables or policies and even seed data instead of only
local mock data. And here's the prompt. Help me configure Superbase for the export delivery app. Inspect the current
project first and propose and implement only the minimum Superbase setup needed for the tutorial flow. Right, we're

### 36:43

going to be using email password off all these tables, public reads, user own tables, basic RLS policies, seed data, and
a bunch of other stuff. So, I'm going to go into plan mode in case it wants to clarify something and double check
something with me for the tutorials. Email password or which local development behavior should the plan use? No email
confirm faster beginner flow users sign up and can use or email confirm. Let's just do no email confirm. That is fine.
Obviously for a production app you might have other requirements and that might include email confirmation. But here I
typically do not do email confirmation. I want something quick and easy so that we can you know get started and hit the
ground running very very quickly. Okay. So we have this minimal minimum superbase setup for the expo delivery tutorial.
But we're going to expand this. Everything looks good. Test plan implementation notes key changes summary

### 37:45

config config superbase only for the tutorial flow. All of this. So we're going to say yes. All right. So it has
implemented the minimum superbase setup. What changed? Added superbase dependencies. All of these things applied
migrations seed data for restaurants. Four menu items. 11 menu modifiers. If we jump into our superbase and we refresh
this, we should see some tables over here created. Okay. And here are tables, addresses, cart items, cards, menu items,
menu modifiers, order items, all of these things, profiles. We have a profile here and that's linked to a user. And so
if we go to O and we go to users here, we should have a user. Okay. Okay. So here we have this delivery tutorial user
and this ID is linked to that profile because this table users is read only.

### 38:45

You can't modify just create users and then you link it to another table in your public schema. And so now that
superbase is ready we can connect our expo app to it in the smallest safe way. The first milestone is not the whole
catalog. It is proving the client environment variables and all sessions all work. Jump into plan mode. And I really
really like plan mode for these prompts. Anytime I'm doing something new such as superbase config or I am doing stitch,
I'm doing UI design. In other words, if I am switching gears, if I'm doing a different part of the app, definitely want
to be in plan mode because we are doing something new. We're not continuing. If I'm continuing and Codeex understands
what I'm trying to do, there's, you know, lesser need for for the plan mode. But if I am switching

### 39:46

gears, I'm trying something new, I'm adding a brand new feature, I'm doing API work, I'm doing config, I'm doing config,
I'm doing something else. Plan mode is paramount, right? So, connect the expo delivery app to Superbase and add the
basic or shell. Add Superbase client setup, add sign up, login, log out, all of these things. So, it's telling us
correctly that the Superbase client and packages are already present. I'm checking the docs read me and it doesn't have
any questions for us because it's kind of up to date, right? It still is going to it's going to do a lot of things. Add
an O provider context that wraps the app alongside card provider. Introduce a basic superbase o layer around the
existing expo delivery app while keeping restaurant browsing card checkout and order tracking mock driven for now. We're
going to go ahead and submit this. It has implemented the superbase osh shell without replacing the mock delivery flow.
We still need to replace

### 40:47

that. We are going to be doing that later. One dashboard step still matters. Disable email confirmation in Superbase O
settings for the smooth simulator signup flow. Okay, so we're going to jump back into Superbase. We are going to go into
authentication. We're going to go into sign in providers and we need to make sure that we disable this confirm email.
We're going to do that and that's going to make the whole flow a lot smoother. So now our app is running here. We're
going to pop. We're going to open up the simulator. Refresh our app. Click this. And there's our app running. Click on
the app. Now, let's try our signin flow. So, let's ask codeex. Give me the username. Use this test account. I'm going to
copy that. Jump back into the app. Paste this. And copy the password. Bite that. Sign in. And here we are signed in.
This is our superbase session. Yeah, we can save it. I guess authors connected mock orders all of this is so the flow is

### 41:50

working. is just a lot of it is just mock right like seated orders right and that's fine that's that's typically how I
build apps I seed them with data so that I can see it being displayed now if we jump into our superbase and go into our
let's see authentication refresh this we have this byte- tutorial user which is what we've used and so now the app
starts moving from mock data to real data the restaurant catalog is the first back and back product milestone because
it's very visible, easy to test, and central to the rest of the app. We're starting with the main discovery screen,
restaurant cards, useful details, search by name or cuisine, loading, empty, and error states, and the app should start
to feel like a real delivery app at this point. And this is the prompt that we want to use. implement the superbase back
restaurant browsing and search milestone for the export delivery app. And we have

### 42:53

our guard rails, right? Because we want to go step by step replace only the list data, all of this superbase restaurants
from Superbase, right? Instead of just mock data that's hardcoded or whatnot, we want to we want to show real data.
Manual simulator checks. Okay. Search for sushi burger Italian filters visible results. Okay, we're going to test that.
Here we have implemented the superbase back restaurant browse search milestone. And if you expand this, you can see it
actually testing the simulator, right? So if you take a look here, you have your simulator screenshot. So, it's
basically testing it, screenshotting it, and making sure that it it looks correct, that everything works, which is
actually pretty cool. And so, now let's go ahead and test it out ourselves, right? Let's go ahead and open this. Let's
restart it. Restart the app. Run this again. Here's the app running. And

### 43:54

there we go. All right. So, let's So, we have here sushi. And this should be coming from Superbase. And if I type sushi,
still not working. But I think it's this filter. No, this filter is also not working. So, a bunch of things that we need
to do. This is not working. So, a lot of things are not working. Let me Let's go ahead and see what were the plans.
Search for sushi filters visible manual browse load Superbase restaurants. Let's first check if these are indeed coming
from Superbase tables restaurants. And we have sushi zen Japanese seafood. Go to our sum as here it says Japanese
seafood rolls and fresh sashimi rating is 4.9 20 to 35 minutes 1 point $1.99 delivery that is correct except the
searching doesn't work. If we come over here pressing enter does not do anything and these filters don't work. Let's go
into browse. Let's type sushi. Actually this works. Japanese

### 44:56

sushi premium. The browse works. Pizza, Mediterranean, healthy. Okay, this works. Sushi. Yeah. So, it's filtering that
and that. So, if I select Japanese, yeah, that works. And that's that's more filters. Categories, delivery time. Okay.
So, this part works. The home does not work. We'll fix it later. Now, at this point, we want to add categories, filters,
favorites, and recently viewed because a delivery app feels thin if the browse screen is only a list. So, this pass adds
the discovery features that make the app feel denser without creating a new product area. Right? So, we're going to be
doing categories, filters, favorites, and recently viewed restaurants and all of that. Make the customer experience feel
more personal and more realistic while still staying inside the same restaurant discovery flow. Add discovery depth to
the restaurant browsing flow

### 45:57

requirements. All of this and we have some guard rails. Jump into plan mode. How should favorites work for this
milestone? I don't want to do a local demo. Okay. I want to I want to make it realistic. Superbase signed in. How should
recently viewed restaurants persist. Local storage. Use device storage. So recent survive app reloads without backed
complexity or session only. This should probably be also superbase, but let's just go with local storage. There's the
plan. So it's going to add a restaurant favorites table. This is the correct way to do it. You want it to be stored in
superbase. Extend restaurant discovery state in the app. Looks good. Let's go ahead and run this. It has implemented the
discovery depth milestone. So these are the key changes. Restaurant favorites expanded the restaurant discovery hook
with superbase favorites. Updated home and browse with all categories ratings. And so if we jump into our simulator,
restart our

### 46:59

app. This is still not working. But we can click on a restaurant and we can favorite it. Okay, this one is a set. Let's
try another one. Let's see. Let's go into browse. How about this pasta? So, I can't seem to un undo it. And this doesn't
work. So, we're going to fix all of that. Two saved places. In fact, let's fix this now. Just copy that. Paste that. and
just say clicking on the heart does not on favorite and the back button does not work. Just run that directly. So these
were actually just static views. They look tapable but had no handlers. So the idea here was that we were going to fix
it later because right now it was not the goal to make them, you know, tapable to handle events. And so seeing this is
important because this way I can do another pass later on in the tutorial where it's going to go through all of these
and

### 48:01

decide if that's supposed to be clickable or tapable or it's just supposed to be a static view. And so this is still
useful because it gives me an idea of how I can do a pass later. And additionally, since we've done this here, Codex
will understand what I'm talking about. So even if this step could have potentially be done later, doing it now is
important because we've given codeex important context when we're going to be doing that final pass before deployment or
a sanity check after deployment. Fixed both issues. Let's go ahead and see. And there it is. And now this works. So once
discovery works, we can build the detail to cart piece. This is where the app becomes interactive because the customer
can open a restaurant, choose menu items, adjust quantities, and see a

### 49:01

totals update. And so for this tutorial, the cart approach should be simple and explainable. Implement the restaurant
detail menu and cart milestone for the export delivery app. Jump into plan mode. Here's the plan. Implement restaurant
detailer and menu loading from Superbase while preserving the current local cart approach. Going to expand that and
we're going to submit this. And so it has implemented the Superbase restaurant detail menu and local cart milestone. It
added a live Superbase menu detail hook here. All of this. And if you scroll up and you expand this, you can see that it
was testing the simulator. It was taking screenshots of the different detail pages your card. So let's go ahead and see
what's happening here. So if we click here, we have this card. We have this. And so now let's say I go into browse. I go
into pasta palace. This restaurant is live but no available menu items. Okay, let's choose another

### 50:02

restaurant. How about Sushi Zen? Still nothing there. This works. How about the burger joint? I think this one should
have it. Now we have burgers. I can click on the burger. I can choose the protein, beef, avocado. This updates. I can
get two burgers, 16 bucks. And I have a burger. I can go into my view cart. And I can switch this. And this updates
automatically. It does not change the delivery fee and the service fee. That remains the same. I can also remove it. And
it is gone. So that's this looks really clean. This this doesn't work yet. We'll do this later. these selectors, but
it's pulling it correctly. Sushi is not there yet, so only the burger is there. Now, the next pass is going to expand
the way ordering works, and it's going to make it feel like a real delivery app. So, this is where customers can expect
item options, cart checks, fees, and a delivery estimate before they commit to checkout. Add realistic

### 51:04

ordering depth to the menu and cart flow. All right. So it has implemented the ordering depth milestone, right? Lots of
validation. Validation validation message is valid for checkout. Required modifier groups now get one default selection
each. Okay. So let's go ahead and check out our app. And here's where we want to test things like customizing an item,
validating the cart, reviewing the fees and delivery estimate, and also confirm that the cart is ready for checkout. So,
let's go ahead and try our burger example here. And let's say we add this add to cart. We have this in cart. And let's
say we want to view our cart. And let's say we want to click here and we want to customize. So, let's say bacon,
avocado, 3.5. These are the modifiers, right? Three $3.50, two bucks, $1.50 and this is required. So, this cannot be
unchecked and this can be

### 52:06

completely unchecked. Yeah, this is very very typical. You know, some things are required. You you you have to choose
something, but other things are optional like utensils and things like that and these extras here. So, this is
important. So, we have this. I'm going to go ahead and add this. So, now I have two burgers. This one and this one. I
can double this. 25 minutes delivery. Two items. I just deleted that. Continue to checkout. And now we have our checkout
here. This is the address. I can change it to my work address. I have my instructions here. This is not editable yet.
Oh, in fact, it is. Leave at the door. This is there. Order summary. We have our payment. This is just hardcoded. We're
not going to be doing payments in this tutorial. We might do it later. So we have a demo card here and then we can place
the order and then we have the order placed. We can also track the order and look at this. We have the whole flow
working. Order received, repairing, out for delivery, delivered, estimated arrival,

### 53:08

22 minutes away from you. Maybe we'll also display a map. We'll see. But so far this order flow is working really,
really nicely. Super happy about it so far. Now, check out is the point where this becomes more than a browsing demo or
we're still using a fake payment, but the order itself should be real data created for the signed in user. And so, the
flow should account for all of that. You know, card confirm delivery details create the order and order items in
Superbase. Update the card and with a confirmation state. So, a lot of that already worked. And so, this next prompt is
going to make sure that there are no edge cases. There's no missing pieces in this entire flow. Implement checkout and
order creation for the Expo delivery app. We have these requirements and we have these guard rails. Do not add real
payments, stripe or anything like that. Jump into plan mode and run that. How

### 54:08

should this tutorial create the superbase order records? sample client inserts, beginner friendly insert order or
database RPC, more robust transactionally, but adds a SQL function migration and more back-end concepts to teach. So,
let's just keep it simple. Okay. And this is going to add real superbase order creation behind the existing mock
checkout UI. Checkout remains fake payment only requires a signed in user writes all of this. Let's go ahead and do
that. It has implemented Superbase back checkout order creation. I did not add payments, none of that refunds, promos.
That's fine. So now let's go ahead and see what we have here. So we're going to jump out and let's go ahead and log in.
This is the user. Okay, there we are. This works. Come back here and let's go ahead and try the flow. So recently viewed
is there. That works. Load the restaurants. We have the sparkling lime. Add to cart. View cart. Continue to

### 55:11

check out. We can send it to or home. This is our order. No modifiers. In fact, do we have a modifier here? View cart.
No, there's no mod. Just special instructions. Add some ice. Something like this. Now we add another one. Or we can
delete this one. Continue to check out. Leave at door. Place order. Track order. We have this 25 minutes estimate and
let's go back. Click on orders. We do not see that order here for some reason. So, that will need to be fixed as well
because that was a brand new order. It was not for a burger. It was for the the rice sparkling line. Maybe it bunched it
up with the other order. So, if I go in here, I still don't see it. So, that is something we'll have to fix later. up.
Right now, checkout feels a lot more complete when the customer can choose where the food is going. Saved addresses and
delivery instructions are very, very useful features for our app. And this

### 56:14

also gives Superbase Off a clear reason to exist beyond login. The signed in user now has personal data that carries
across orders and makes the app feel much more persistent. Add saved addresses and delivery instructions to the checkout
floor. Requirements. These are the requirements. Let's go ahead jump into plan mode. Run that. So, it has implemented
saved addresses and delivery instructions in checkout. Let's go ahead and see how this works. Jump back to our home
screen here and let's go ahead and try the flow. Maybe creating a saved address, adding delivery instructions, and
placing an order using that address. All right, so let's try this burger here. Let's add this add to cart. View cart.
Continue to checkout. And now we have this selected. I can add an address here. Okay, look at this. So let's say I want
to ship to this is work. Let's say 10 West Street, New York. New York one. Call the the

### 57:17

door. Ring the bell. Four, leave with the doorman. Of course, everybody has a doorman, right? Save address. And now we
have this address here. So, I can add multiple addresses. I can add another address. I can cancel this. Really nice. Or
I can keep it set it to home. Okay. I can set this to work. Leave with the door man. 25 minutes. Place order. Track
order. And here's the order. Smokehouse. Yeah, that's the that's the burger barbecue. 25 minutes. Looks good. Now, if we
go back and we go into orders, we still do not see it here. And this is something that we have to fix, but we're getting
closer. We are adding the the all important depth to our app. And so, after checkout creates orders, the customer needs
somewhere to see them. And this is where we're going to configure the account or orders area and connect the
confirmation flow to order history. Build the profile order history

### 58:20

and simple tracking milestone for the export delivery app requirements. All of this and we have some guardrails. Do not
add driver tools, restaurant admin, maps routing, live GPS, at least for now plan mode. We're going to be replacing the
remaining mock profile order services with superbase backed account order history and order detail data. And it has
implemented the profile order history and simple tracking. And now let's go ahead and test that whole order flow. And
let's ensure that that orders that bug that we kept having is now finally patched. So let's go ahead and refresh our
app. Restart it. If we go into orders, this is what we see. Okay, so we don't have that message. We have the smokehouse
barbecue on the sparkly line. So it has already been fixed. Okay, because the data wasn't superbase. It was just this
page kept showing fake data, mock data. So we

### 59:22

can refresh this here. We can click here and we can see leave with the doorman demo tracking. Use the tutorial. So we
can have advanced demo status here. So, this looks good now. Yeah. So, we can create a new order. And that should create
a brand new order. Classic cheeseburger. Add to cart. View cart. Continue to check out. Going to send it to work. Place
order. Track order. And this is our order over here. Okay. So, now if I go back back again and go into orders, it should
be here. Let's refresh it. And there it is. Classic cheeseburger. And I can see 25 minutes sent to the kitchen. Order
received. Preparing. So we have our delivery status there. Speaking of order status, you would probably agree with me
that tracking screen becomes much more convincing when the order has a visible timeline. We do not need live GPS or a
driver app, but we do need the customer to understand

### 01:00:24

what is happening after checkout. And so what we want to do is we want to make it a little bit more user friendly so
that they know exactly what's happening with their order because that's the part of the app that they're going to be
checking constantly after placing the order. I know that that is something that I do constantly. Add an order status
timeline and demo status updates. Show a clear timeline for place preparing out for delivery and delivered. Persist
status history. Do not add driver accounts. Real notifications. Live GPS. Jump into plan mode. Probably we don't really
need plan mode, but why not polish the existing tracking flow into a clear tutorial grade status timeline. So it has
implemented the status timeline polish. So let's go ahead and see how this looks. And look at this. That looks a lot
better. Place preparing out for delivery. Delivered. This looks

### 01:01:25

so much better. And let's go ahead and see. Check out some other orders. Look at this place. Preparing. Looks awesome.
Out for delivery now. And now it's delivered. So, this is a way to test out the orders to to kind of move it along the
steps. If we go back order, let's go ahead and refresh it. So, this is delivered. This is preparing. Advanced demo
status. And now it's out for delivery. And now it is delivered. Really nice. Refresh this. So now we have two orders
delivered really clean. Now in this next pass we are going to be doing a little bit of testing and debugging. Okay. And
this is a pass where codeex is going to prove to be very very valuable. So instead of adding more features, we need to
inspect the real implementation, find the weakest part of the flow and explain what is probably going wrong and patch
only what needs to be patched. And so the final test needs to cover the whole customer path. Applaunch off,

### 01:02:28

restaurant delivery, favorites, detail, item customization, on and on and on. Everything that we've been building so
far. Debug, review, and verify the Expo delivery app end to end in the iOS simulator. Inspect the current implementation
first. Diagnose issues before changing code. And we don't even have any guardrails yet, right? because we're not adding
features. We're mostly testing. Make the smallest safe fix or polish pass needed to stabilize the current workflow. Then
produce the final simulator test checklist. So, I'm going to jump into plan mode for this. Here's the plan. Current
inspection shows the core app is structurally sound. Typescript and it has some key fixes. fix checkout navigation
polish and a bunch of other fixes. All right, so it has implemented the stabilization plan, changed a bunch of things.
Check out back arrow is now a

### 01:03:28

real tapable button with fallback back to cardart behavior. Updated this signed in checkout copy updated this timeline
connector now fills only for completed steps. All of this stuff final checklist to run manually tabs all open. Home
browse cards open details. So let's take a look. So all of this opens. Search behave as expected. So let's see if this
finally works. This still doesn't work. This needs to be fixed. We're going to fix that. This is still not filtering.
Search on home tab doesn't work. Filtering doesn't work. Does not work. And then I cannot select the address here.
Cannot select delivery address. Let's go ahead and have it fix that. Those are the main kind of bugs that I see right
away. We still need to test and see if there are any other bugs, but that is the main kind of, you know, main issues
that we need to have fixed. And yes, they are caused by interaction design, not missing Superbase data. Yeah, that's
pretty much it. Our

### 01:04:29

Superbase end is completely fine. A lot of these bugs are purely UI stuff, purely interaction design. So, it has
implemented the fix. Home now switches into a clear results mode. as soon as search category filters or sort are active.
Let's see. There we go. That seems good. This should also work. Free delivery is here. Let's go ahead and reload this
just to make sure. All right. Here's our app. So now if I click here, this still does not work. But this should work. So
if I type burger, it works. It switches into results mode. I can clear this. Comes back. I can do ratings pre-dely. That
seems like it's working. I have my favorites. I can unfavor this. Now it's gone. I can clear all this. This works. And I
can sort by lowest fee, recommended, highest rated, etc. The only thing that doesn't work is that is I cannot select the
address. So, let's go ahead and have it fixed. And

### 01:05:29

this doesn't work. And clicking trying to select an address does nothing. Let's go ahead and just squash these bugs. All
right. We fixed the address selection issue. There it is. That's much better. This thing doesn't work. Let's go ahead
and have this fixed. Clicking on the filters icon does not do anything. Let's just squash that. All right. So, that is
fixed. The filter icon on home is now a real tapable button. Much better. Well, yeah, this should disappear as well. So,
let's do this. I don't That should never be there. This should not be displayed. Just make the filter icon different
color when it is selected so we can see the state change. It's already done. Look at. And next, we want to do a final
simulator pass. And we're going to be running the app like a real user would. The Expo app should start cleanly. The

### 01:06:30

Superbase environment should be configured. and the full flow should work in the iOS simulator from browsing to
delivered order. Run the final iOS simulator demo pass for the export delivery app requirements. Do not add new product
features during the final demo pass. Let's go ahead and run that. Let's jump into plan mode just in case. We probably do
not need it for a simple prompt such as this one, but why not? So, I ran the safe nonmutating final demo checks.
Everything confirmed. Superbase read only checks. Everything is done. So let's go ahead and do a quick pass. Let me
restart the app. All right. So we can select this work. We can select unselect this. We can order some sushi. We don't
have any items for sushi. That's fine. I know this works cuz we can select a burger. Click here. Add to cart. View cart.
I can add another burger. I can select my work because that's the that's the

### 01:07:31

address that I've selected on the on the main screen. I can change my delivery instructions, place order, track order.
This is for testing. This is actually really nice. This is not something I believe I asked for. And so this is really
nice. Out for delivery. If we come back and we go into orders, we should see that order as being out for delivery. This
one. And then we can scroll down and do advanced. Advance the status. And it is delivered. Come back here. Refresh this.
Delivered. Four superbase orders. Two safe places. Latest order. We can log out. It looks really, really clean. Now that
the demo works, this is also a good time to work on some improvements, some features that we may launch in the next
version of the app. Create or update docs with the selected high impact loweffort improvement backlog for the expo
delivery app. Okay. Requirements guard rails. Do not

### 01:08:33

implement the two items. Do not include secrets. Do not add payments. Well, payments is actually a good idea to do. And
in fact, what I'm going to do is I'm going to remove this guard rail. Let it just include anything that it wants to
include. And if there's enough interest in this video, I will also do a second part where I am going to implement all of
these extra features that make up a real production ready delivery app such as payments, delivery tracking, maps,
anything that you can imagine that you're used to whenever you're using Uber Eats or Glov or anything of that sort.
Leave a like on this video, leave a comment, and if there's enough interest, I'm definitely going to be doing a part two
of this series. So, let's go ahead and keep it in plan mode. Run this and see what it comes up with. It's nice that it's
going to be categorizing them as a problem, improvement, and verify. And typically, that's exactly what you want to do.

### 01:09:34

Either it is a problem, I bug, or it's an improvement. And then we also have verify step here. I'm going to submit that.
Let it create that file for next time. Okay. And it has created this file. We can click here. Open this file. And this
is our file. This backlog is a beginnerfriendly local expo plus superbase food delivery tutorial app. These are the high
impact quick wins home filter icon state problem. Home delivery clarity delivery address picker clarity. Lots of things
later or out of scope ideas. Superbase card persistence profile address. So like I said, if there's enough interest for
a part two, I will make a super comprehensive part two tutorial where we're going to have real time tracking maps, you
name it. Anything that you can think of that you are, you know, you've seen in other apps, we're going to do just that.
So definitely like this video, leave a

### 01:10:34

comment to show your appreciation. And if you're interested in getting access to all of these prompts, I'm going to be
making available the entire prompt pack in our amazing Patreon community. So, click the first link, join our amazing
Patreon community. We got an awesome awesome community, lots and lots of value, lots and lots of extra content. Plus,
it's a great way to support this channel and support my work. So, hopefully I'll see you inside.
