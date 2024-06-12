from lib.db.app import get_session, init_db
from lib.db.models import Ward, Patient

def debug():
    init_db()
    session = get_session()
    # Add debug code here
    ward = Ward(ward_number=1)
    session.add(ward)
    session.commit()

if __name__ == '__main__':
    debug()
