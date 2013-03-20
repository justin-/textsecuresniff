While debugging an unrelated issue for WhisperSystems' [TextSecure](https://github.com/WhisperSystems/TextSecure/), I noticed that keypresses were being written to the Android logfile during the passphrase prompt. Turns out _this was a vulnerability with my specific phone and NOT the TS application._ Furthermore, the issue appears to be isolated to use of the hardware keyboard. The logfile functions as a ring buffer and must be copied shortly after the passphrase is entered.

* _dumplog_ - Copy the Android logfile to the sdcard
* _tssniff_ - Parse the logfile for keypresses

Again, this vulnerability is the fault of my phone and NOT the TS app.