// add socketclient java - simple java tcp soket client
import java.io.PrintWriter;
import java.net.Socket;

public class SocketClient {
	public static void main(Strings[] args){
		try{
			Socket s = new Socket ("$IP", 5555);
			PrintWriter out = new PrintWriter(s..getOutStream(), true);
			out.println("Hello World!")l; // change the message
			s.close();
	} catch(Exception e) {
	}
	}
}

