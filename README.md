# Documentation for saadat.dev
> Python 3.6+ | MongoDB & redis | GDRP Compliant

## Used Frameworks / Technologies

#### Backend
- Sanic
	- The _(Python 3.6+)_ web framework of choice. It's basically Flask but entirely async and powered by uvloop. Sanic's reliably fast, secure and extensive. Who needs node if you have sanic.
- Nginx (reverse proxy)
- redis
	- Being the ultra-fast i/o database of choice, redis is used as IP cache for the custom anti-spam measurement. I could've used existing solutions but then again, no fun if you don't do it yourself.
- MongoDB
	- Deployed as message broker, it caches messages sent through the contact form, which then get handled by the custom emailing solution _...which isn't really an email agent._ It's a discord bot fetching and relaying the messages, go [HERE](https://github.com/mass1ve-err0r/Mango) to view the source.

#### Frontend

- Jinja2
	- The underlying templating engine. I used it in other projects before and it's just super easy to work with and allows for easy python interop. Just a classic.
- Bootstrap v5
	- Simple toolkit to design and work with. Call it basic but it works.

## Extra Notes

### Contact Form Safety
The contact form is probably the weakest link in any website because you have to deal with form validation to avoid injections. To my knowledge, my website is safe to these types of attacks because they're stored as plaintext strings, even if you use postman you **cannot** force the form to accept any:
- Message with over 1500 chars.
- Subject with over 200 chars.
- EMail over 200 chars.

or empty fields. Server-Side checks are additionally there for the contact route as it's the only one accepting POSTs.

### IP Logging / Anti-Spam
Whenever you open the contact page, your actual IP will be logged to redis. This is for safety reasons to avoid people sending me junk / bot my website and thus cause outages or overly big spam. If you peek throught he code you'll see per IP the limit is 200 accesses per day, regardless if you send me an email or not.


### Why Python and not nodejs?
Because I refuse to use JavaScript whenever possible. Python (can) be faster, the [Japronto](https://github.com/squeaky-pl/japronto) project is a perfect example of this, it's just better **in my opinion.**
