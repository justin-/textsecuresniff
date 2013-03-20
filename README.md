While debugging an unrelated issue for WhisperSystems' [TextSecure](https://github.com/WhisperSystems/TextSecure/), I noticed that keypresses were being written to the Android logfile during the passphrase prompt. Turns out __this was a vulnerability with my specific phone and NOT the TS application.__ Furthermore, the issue appears to be isolated to use of the hardware keyboard. The logfile functions as a ring buffer and must be copied shortly after the passphrase is entered.

* __dumplog__ - Copy the Android logfile to the sdcard
* __tssniff__ - Parse the logfile for keypresses

Again, this vulnerability is the fault of my phone and NOT the TS app.