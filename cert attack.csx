// generate a 4096 bit RSA key with SHA512 hash
var ca = CertificateUtils.GenerateCACert("CN=MyTestCA", 4096, CertificateHashAlgorithm.Sha512);
//Export that shit!! With PFX with no password
File.WriteAllBytes("ca.pfx", ca.ExportToPFX());
//Export Public Cert to a PEM file
File.WriteAllTexts("ca.crt", ca.ExportToPEM());

//last but not least, add TLS layer as in Listening
CertificateManager.SetRootCert("ca.pfx");

// all generated certs will be your cert, but next run the commmand or save as 

//generate_ca_cert.csx

//then import it to certmgr.msc

//choose trusted root cerficication authorities -> Certificates
//then click action -> all tasks -> import
//enter ca.crt, then click next
// place in trust root certification authorities
// then finish
//but becareful, if someone gets your private key, game over, they can attack you 