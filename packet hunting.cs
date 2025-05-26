// SocksProxy.csx -Simple SOCKS proxy
// Exposed methods methods loke WriteLines and WriteBack
useing static System.Console;
useing static CAANAPE.Cli.ConsoleUtils;

// Create the SOCKs proxy templet
car templet = new SocksProxyTemplate();
template.LocalPort = LOCALPORT;

//make the proxy service
var service = template.Create();
service.Start();
WriteLines("Capture {0}", service);
WriteLines("Press Enter to exit.....");
ReadLine();
service.Stop();

// dump packets
var packets = service.Packets;
WriteLine("Captured {0} packets", packets.Count);
Write.Packets(packets);


