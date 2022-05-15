import { Col, Container, Row } from 'react-bootstrap';

const videoFeed = 'http://localhost:3001/video_feed';

export default function VideoScreen() {
  return (
    <Container>
      <Col>
        <span className="title">YourFitnessPal</span>
        <span className="sub-title">HawkHacks 2022</span>
        <Row>
          <img className="video-feed" src={videoFeed} alt="Realtime Video" />
        </Row>
      </Col>
    </Container>
  );
}
