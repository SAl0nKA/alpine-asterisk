import os
DEFAULT_PATH = "/etc/asterisk/"

def main():
    #check if path exists
    if not os.path.exists(DEFAULT_PATH):
        os.makedirs(DEFAULT_PATH)

    #check if the folder is empty
    if any(os.listdir(DEFAULT_PATH)):
       print("Folder is not empty, skipping creating sample files")
       return

    print("Creating sample files")
    with open(DEFAULT_PATH + "pjsip.conf", 'w') as file:
        file.write(""";===============  GLOBAL VARIABLES
[global]
type=global
;keep_alive_interval=60


;===============  SYSTEM VARIABLES

[system]
type=system

;===============  TRANSPORT

[transport-udp-ipv4]
type=transport
protocol=udp
bind=0.0.0.0
tos=cs3

[transport-udp-ipv6]
type=transport
protocol=udp
bind=::
tos=cs3

[transport-tcp-ipv4]
type=transport
protocol=tcp
bind=0.0.0.0
tos=cs3

[transport-tcp-ipv6]
type=transport
protocol=tcp
bind=::
tos=cs3


;===============  ENDPOINT TEMPLATES

[endpoint](!)
type=endpoint
context=dokovanie
direct_media=no
rtp_ipv6=yes
disallow=all
allow=g722,alaw,ulaw,g729,h264
tos_audio=ef
tos_video=af41
cos_audio=5
cos_video=4

[endpoint-udp](!,endpoint)
transport=transport-udp-ipv4

[endpoint-tcp](!,endpoint)
transport=transport-tcp-ipv4

[auth](!)
type=auth
auth_type=userpass

[aor](!)
type=aor
max_contacts=5
remove_existing=yes
default_expiration=3600

;===============  CONTACTS
""")

    with open(DEFAULT_PATH + "asterisk.conf", 'w') as file:
        file.write("""[directories](!)
astcachedir => /var/cache/asterisk
astetcdir => /etc/asterisk
astmoddir => /usr/lib/asterisk/modules
astvarlibdir => /var/lib/asterisk
astdbdir => /var/lib/asterisk
astkeydir => /var/lib/asterisk
astdatadir => /var/lib/asterisk
astagidir => /var/lib/asterisk/agi-bin
astspooldir => /var/spool/asterisk
astrundir => /var/run/asterisk
astlogdir => /var/log/asterisk
astsbindir => /usr/sbin

[options]
;verbose = 3
;debug = 3
;trace = 0              ; Set the trace level.
;refdebug = yes			; Enable reference count debug logging.
;alwaysfork = yes		; Same as -F at startup.
;nofork = yes			; Same as -f at startup.
;quiet = yes			; Same as -q at startup.
;timestamp = yes		; Same as -T at startup.
;execincludes = yes		; Support #exec in config files.
;console = yes			; Run as console (same as -c at startup).
;highpriority = yes		; Run realtime priority (same as -p at
				; startup).
;initcrypto = yes		; Initialize crypto keys (same as -i at
				; startup).
;nocolor = yes			; Disable console colors.
;dontwarn = yes			; Disable some warnings.
;dumpcore = yes			; Dump core on crash (same as -g at startup).
;languageprefix = yes		; Use the new sound prefix path syntax.
;systemname = my_system_name	; Prefix uniqueid with a system name for
				; Global uniqueness issues.
;autosystemname = yes		; Automatically set systemname to hostname,
				; uses 'localhost' on failure, or systemname if
				; set.
;mindtmfduration = 80		; Set minimum DTMF duration in ms (default 80 ms)
				; If we get shorter DTMF messages, these will be
				; changed to the minimum duration
;maxcalls = 10			; Maximum amount of calls allowed.
;maxload = 0.9			; Asterisk stops accepting new calls if the
				; load average exceed this limit.
;maxfiles = 1000		; Maximum amount of openfiles.
;minmemfree = 1			; In MBs, Asterisk stops accepting new calls if
				; the amount of free memory falls below this
				; watermark.
;cache_media_frames = yes	; Cache media frames for performance
				; Disable this option to help track down media frame
				; mismanagement when using valgrind or MALLOC_DEBUG.
				; The cache gets in the way of determining if the
				; frame is used after being freed and who freed it.
				; NOTE: This option has no effect when Asterisk is
				; compiled with the LOW_MEMORY compile time option
				; enabled because the cache code does not exist.
				; Default yes
;cache_record_files = yes	; Cache recorded sound files to another
				; directory during recording.
;record_cache_dir = /tmp	; Specify cache directory (used in conjunction
				; with cache_record_files).
;transmit_silence = yes		; Transmit silence while a channel is in a
				; waiting state, a recording only state, or
				; when DTMF is being generated.  Note that the
				; silence internally is generated in raw signed
				; linear format. This means that it must be
				; transcoded into the native format of the
				; channel before it can be sent to the device.
				; It is for this reason that this is optional,
				; as it may result in requiring a temporary
				; codec translation path for a channel that may
				; not otherwise require one.
;transcode_via_sln = yes	; Build transcode paths via SLINEAR, instead of
				; directly.
;runuser = asterisk		; The user to run as.
;rungroup = asterisk		; The group to run as.
;lightbackground = yes		; If your terminal is set for a light-colored
				; background.
;forceblackbackground = yes     ; Force the background of the terminal to be
                                ; black, in order for terminal colors to show
                                ; up properly.
;defaultlanguage = en           ; Default language
documentation_language = en_US	; Set the language you want documentation
				; displayed in. Value is in the same format as
				; locale names.
;hideconnect = yes		; Hide messages displayed when a remote console
				; connects and disconnects.
;lockconfdir = no		; Protect the directory containing the
				; configuration files (/etc/asterisk) with a
				; lock.
;stdexten = gosub		; How to invoke the extensions.conf stdexten.
				; macro - Invoke the stdexten using a macro as
				;         done by legacy Asterisk versions.
				; gosub - Invoke the stdexten using a gosub as
				;         documented in extensions.conf.sample.
				; Default gosub.
;live_dangerously = no		; Enable the execution of 'dangerous' dialplan
				; functions and configuration file access from
				; external sources (AMI, etc.) These functions
				; (such as SHELL) are considered dangerous
				; because they can allow privilege escalation.
				; Configuration files are considered dangerous
				; if they exist outside of the Asterisk
				; configuration directory.
				; Default no
;entityid=00:11:22:33:44:55	; Entity ID.
				; This is in the form of a MAC address.
				; It should be universally unique.
				; It must be unique between servers communicating
				; with a protocol that uses this value.
				; This is currently is used by DUNDi and
				; Exchanging Device and Mailbox State
				; using protocols: XMPP, Corosync and PJSIP.
;rtp_use_dynamic = yes          ; When set to "yes" RTP dynamic payload types
                                ; are assigned dynamically per RTP instance vs.
                                ; allowing Asterisk to globally initialize them
                                ; to pre-designated numbers (defaults to "yes").
;rtp_pt_dynamic = 35		; Normally the Dynamic RTP Payload Type numbers
				; are 96-127, which allow just 32 formats. The
				; starting point 35 enables the range 35-63 and
				; allows 29 additional formats. When you use
				; more than 32 formats in the dynamic range and
				; calls are not accepted by a remote
				; implementation, please report this and go
				; back to value 96.
;hide_messaging_ami_events = no;  This option, if enabled, will
                ; suppress all of the Message/ast_msg_queue channel's
                ; housekeeping AMI and ARI channel events.  This can
                ; reduce the load on the manager and ARI applications
                ; when the Digium Phone Module for Asterisk is in use.

; Changing the following lines may compromise your security.
;[files]
;astctlpermissions = 0660
;astctlowner = root
;astctlgroup = apache
;astctl = asterisk.ctl
""")
    with open(DEFAULT_PATH + "extensions.conf", 'w') as file:
        file.write("""[global]

[dokovanie]
exten => 100,1,Dial(PJSIP/test,20)""")

    with open(DEFAULT_PATH + "modules.conf", 'w') as file:
        file.write(""";
; Asterisk configuration file
;
; Module Loader configuration file
;

[modules]
autoload=yes
;
; Any modules that need to be loaded before the Asterisk core has been
; initialized (just after the logger initialization) can be loaded
; using 'preload'.  'preload' forces a module and the modules it
; is known to depend upon to be loaded earlier than they normally get
; loaded.
;
; NOTE: There is no good reason left to use 'preload' anymore.  It was
; historically required to preload realtime driver modules so you could
; map Asterisk core configuration files to Realtime storage.
; This is no longer needed.
;
;preload = your_special_module.so
;
; If you want Asterisk to fail if a module does not load, then use
; the "require" keyword. Asterisk will exit with a status code of 2
; if a required module does not load.
;
;require = chan_pjsip.so
;
; If you want you can combine with preload
; preload-require = your_special_module.so
;
;load = res_musiconhold.so
;
; Load one of: alsa, or console (portaudio).
; By default, load chan_console only (automatically).
;
noload = chan_alsa.so
;noload = chan_console.so
;
; Do not load res_hep and kin unless you are using HEP monitoring
; <http://sipcapture.org> in your network.
;
noload = res_hep.so
noload = res_hep_pjsip.so
noload = res_hep_rtcp.so
;
; Do not load chan_sip by default, it may conflict with res_pjsip.
; noload = chan_sip.so
;
; Load one of the voicemail modules as they are mutually exclusive.
; By default, load app_voicemail only (automatically).
;
;noload = app_voicemail.so
noload = app_voicemail_imap.so
noload = app_voicemail_odbc.so
""")

#todo add voicemail

if __name__ == '__main__':
    main()

