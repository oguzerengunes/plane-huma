-- Hüma davet kodu modülü — DB spec (Plane fork veya Supabase)
-- Plane'de departman = project_project(id). Supabase sıfırdansa departments(id).

CREATE TABLE department_invite_code (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id UUID NOT NULL REFERENCES project_project(id) ON DELETE CASCADE,
  code_hash CHAR(64) NOT NULL UNIQUE,
  code_prefix CHAR(4) NOT NULL,
  created_by UUID NOT NULL,
  expires_at TIMESTAMPTZ NOT NULL,
  max_uses INT NOT NULL DEFAULT 50 CHECK (max_uses > 0),
  use_count INT NOT NULL DEFAULT 0 CHECK (use_count >= 0),
  require_approval BOOLEAN NOT NULL DEFAULT FALSE,
  is_revoked BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  revoked_at TIMESTAMPTZ,
  CHECK (expires_at > created_at)
);
CREATE INDEX idx_invite_code_project ON department_invite_code(project_id) WHERE is_revoked = FALSE;
CREATE INDEX idx_invite_code_expiry ON department_invite_code(expires_at) WHERE is_revoked = FALSE;

CREATE TABLE department_join_request (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  code_id UUID NOT NULL REFERENCES department_invite_code(id) ON DELETE CASCADE,
  project_id UUID NOT NULL,
  user_id UUID NOT NULL,
  status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending','approved','rejected')),
  decided_by UUID,
  decided_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (code_id, user_id),
  CHECK ((status = 'pending' AND decided_by IS NULL AND decided_at IS NULL)
      OR (status IN ('approved','rejected') AND decided_by IS NOT NULL AND decided_at IS NOT NULL))
);
CREATE INDEX idx_join_req_pending ON department_join_request(project_id, status) WHERE status = 'pending';
CREATE INDEX idx_join_req_user ON department_join_request(user_id, status);

-- Atomik kontenjan artırma (race-safe):
-- UPDATE department_invite_code SET use_count = use_count + 1
-- WHERE id = :id AND use_count < max_uses AND is_revoked = FALSE AND expires_at > now()
-- RETURNING id;
