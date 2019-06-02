package connection;

public class Jython {

	public static void main(String[] args) {
		Tensorflow tf = new Tensorflow();
		
		String image = "C:\\Users\\sangw\\OneDrive\\Desktop\\data\\5.jpg";
		
		//상의 분석
		tf.Upper_Tensorflow(image);

		//하의 분석
		tf.Lower_Tensorflow(image);
		
		//사진 복구
		tf.restore(image);
	}

}
